DROP TABLE IF EXISTS `fee_details`;
CREATE TABLE `fee_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(30) DEFAULT NULL,
  `fee_amount` varchar(10) DEFAULT NULL,
  `pay_date` varchar(30) DEFAULT NULL,
  `pay_mode` varchar(20) DEFAULT NULL,
  `month_name` varchar(10) DEFAULT NULL,
  `f_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
DROP TABLE IF EXISTS `profile`;
CREATE TABLE `profile` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(500) DEFAULT NULL,
  `cont` varchar(300) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `stat` varchar(500) DEFAULT NULL,
  `dist` varchar(500) DEFAULT NULL,
  `pin` varchar(200) DEFAULT NULL,
  `loaction` varchar(5000) DEFAULT NULL,
  `about` varchar(4500) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
DROP TABLE IF EXISTS `room_allocation`;
CREATE TABLE `room_allocation` (
  `roomid` varchar(30) DEFAULT NULL,
  `userid` varchar(50) DEFAULT NULL,
  `checkin` varchar(10) DEFAULT NULL,
  `checkout` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL
);
DROP TABLE IF EXISTS `room_details`;
CREATE TABLE `room_details` (
  `room_no` varchar(30) DEFAULT NULL,
  `room_type` varchar(50) DEFAULT NULL,
  `total_bed` varchar(10) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL
);
DROP TABLE IF EXISTS `rules`;
CREATE TABLE `rules` (
  `userid` varchar(30) DEFAULT NULL,
  `rules` varchar(500) DEFAULT NULL
);
DROP TABLE IF EXISTS `signup`;
CREATE TABLE `signup` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(500) DEFAULT NULL,
  `sec_q` varchar(500) DEFAULT NULL,
  `ans` varchar(500) DEFAULT NULL,
  `pass` varchar(200) DEFAULT NULL,
  `user_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `userid` varchar(30) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `user_cont` varchar(15) DEFAULT NULL,
  `user_gender` varchar(10) DEFAULT NULL,
  `user_dob` varchar(30) DEFAULT NULL,
  `user_blood_grp` varchar(10) DEFAULT NULL,
  `user_f_name` varchar(100) DEFAULT NULL,
  `user_m_name` varchar(100) DEFAULT NULL,
  `user_p_contact` varchar(20) DEFAULT NULL,
  `user_pic` longblob,
  `user_addhar` varchar(15) DEFAULT NULL,
  `user_street` varchar(200) DEFAULT NULL,
  `user_dstate` varchar(500) DEFAULT NULL,
  `user_pin` varchar(20) DEFAULT NULL,
  `user_local_guard` varchar(100) DEFAULT NULL,
  `user_local_guard_cont` varchar(100) DEFAULT NULL,
  `user_local_guard_add` varchar(500) DEFAULT NULL
);
commit;