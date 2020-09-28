/*
Total unique session IDs ignoring the session-break at midnight (fullVisitorId+visitId).

Total unique session IDs including the session-break at midnight (fullVisitorId+visitStartTime).

Count of sessions excluding sessions comprising of non-interaction hits only (totals.visits).

fullVisitorId- the unique visitor ID (aka client ID). Count of this can give us unique users number, but not sessions number.
visitId- An identifier for this session. Count of this may give us total sessions number.
totals.visits- The number of sessions (for convenience). This value is 1 for sessions with interaction events. The value is null if there are no interaction events in the session.

*/

-- 1. How many sessions are there?
 SELECT 
  -- count(visitId) as total_sessions
  count(CONCAT(cast(visitId as string),"-",fullVisitorId)) AS sessionId

 FROM
  `dhh-analytics-hiringspace.GoogleAnalyticsSample`.ga_sessions_export
  -- 216672 


-- 2. ​How many sessions does each visitor create?
 SELECT 
   fullvisitorid,
    count(visitId) as sessions_per_visitor
 FROM
  `dhh-analytics-hiringspace.GoogleAnalyticsSample`.ga_sessions_export
  group by 1 
  order by 1

-- 3. How much time does it take on average to reach the order_confirmation screen per session (in minutes)?
-- time for the hits when ordered, hits.time contains number of milliseconds since first hit, therefore to get time of transactions
select avg(time) / 60000 as avg_time_per_session from (
select fullvisitorid,visitId, min(h.time) as time    from  `dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export` a, unnest(hit) as h
WHERE h.eventCategory in ('ios.order_confirmation', 'android.order_confirmation')
group by 1,2 ) as temp1
-- 10.147499071894604


/*
4. By using the ​GoogleAnalyticsSample​ data and BackendDataSample tables, analyse
how often users tend to change their location in the beginning of their journey (screens like home and listing) versus in checkout and on order placement and demonstrate the the deviation between earlier and later inputs (if any) in terms of coordinates change. Then, using the ​BackendDataSample​ table, see if those customers who changed their address ended placing orders and if those orders were delivered successfully, if so, did they match their destination.

eventCategory cnt
ios.onboarding  1
ios.order_confirmation  1
android.NA  1
android.onboarding  3
ios.other 18
ios.shop_details  19
ios.user_account  29
android.null  347
android.user_account  1451
android.checkout  4478
android.home  5585
ios.checkout  13398
ios.home  15477
android.shop_list 34467
ios.shop_list 46386
*/

-- initial page was home/search/shop_list
-- later becomes: checkout/order_confirmation


WITH
  address_update AS(
  SELECT
    fullvisitorid,
    visitId,
    hitNumber,
    eventCategory,
    eventLabel,
    ROW_NUMBER() OVER (PARTITION BY fullvisitorid, visitId ORDER BY hitNumber DESC) AS seqnum
  FROM
    `dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export` t,
    UNNEST(hit) hit
  WHERE
    hit.eventAction IN ('address_update.submitted',
      'address.submitted') ),
  orders AS (
  SELECT
    fullvisitorid,
    visitId,
    hit.transactionId
  FROM
    `dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export` t,
    UNNEST(t.hit) hit
  WHERE
    transactionId IS NOT NULL )
SELECT
  a.fullvisitorid,
  a.visitId,
  hitNumber,
  CASE
    WHEN eventCategory = 'ios.checkout' THEN TRUE
    WHEN eventCategory = 'android.checkout' THEN TRUE
    WHEN eventCategory = 'ios.order_confirmation' THEN TRUE
    WHEN eventCategory = 'android.order_confirmation' THEN TRUE
  ELSE
  FALSE
END
  AS lateAddressChange,
  eventLabel,
  transactionId,
  CASE
    WHEN status_id = 24 THEN TRUE
    WHEN status_id IS NULL THEN NULL
  ELSE
  FALSE
END
  AS successfulDelivery,
  declinereason_code,
  declinereason_type,
  geopointCustomer,
  geopointDropoff,
  ST_DISTANCE(geopointCustomer,
    geopointDropoff) AS diff_distance
FROM
  address_update a
LEFT JOIN
  orders b
ON
  a.fullvisitorid = b.fullvisitorid
  AND a.visitId = b.visitId
LEFT JOIN
  `dhh-analytics-hiringspace.BackendDataSample.transactionalData` be
ON
  b.transactionId = be.frontendOrderId
WHERE
  seqnum = 1



