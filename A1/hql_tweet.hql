CREATE TABLE tweets(tweet STRING);

LOAD DATA INPATH 'input/files/*'
OVERWRITE INTO TABLE tweets;

CREATE TABLE prons(pron STRING, freq INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

ADD FILE mapper.py;

INSERT OVERWRITE TABLE prons
SELECT
  TRANSFORM (tweet)
  USING 'python3 mapper.py'
  AS (pron, freq)
FROM tweets;

SELECT pron, count(*)
FROM prons
GROUP BY pron;