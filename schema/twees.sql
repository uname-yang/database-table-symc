
DROP DATABASE IF EXISTS twee;
CREATE DATABASE twee;
USE twee;


CREATE TABLE twees (
  twee_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  id_str VARCHAR(20) NOT NULL,
  text VARCHAR(500) NOT NULL,
  source VARCHAR(200) NOT NULL,
  user VARCHAR(20) NOT NULL,
  retweet_count INT NULL,
  favorite_count INT NULL,
  lang VARCHAR(10) NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (twee_id),
  KEY idx_user_name (user)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


select id_str,text,user,favorite_count,created_at from twees;
select count(*) from twees;
