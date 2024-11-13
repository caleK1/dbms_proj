-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: dbms_proj
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adm_general`
--

DROP TABLE IF EXISTS `adm_general`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adm_general` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `adm` float DEFAULT NULL,
  `wadm` float DEFAULT NULL,
  `adjusted_adm` float DEFAULT NULL,
  `adm_pde_363` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `adm_general_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `adm_grades`
--

DROP TABLE IF EXISTS `adm_grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adm_grades` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `adm_pre_kindergarten_ht` float DEFAULT NULL,
  `adm_pre_kindergarten_ft` float DEFAULT NULL,
  `adm_kindergarten_ht4` float DEFAULT NULL,
  `adm_kindergarten_ft4` float DEFAULT NULL,
  `adm_kindergarten_ht5` float DEFAULT NULL,
  `adm_kindergarten_ft5` float DEFAULT NULL,
  `adm_elementary` float DEFAULT NULL,
  `adm_secondary` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `adm_grades_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `aid_ratio`
--

DROP TABLE IF EXISTS `aid_ratio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aid_ratio` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `market_value` float DEFAULT NULL,
  `personal_income` float DEFAULT NULL,
  `wadm` float DEFAULT NULL,
  `mv_per_wadm` float DEFAULT NULL,
  `market_value_aid_ratio` float DEFAULT NULL,
  `pi_per_wadm` float DEFAULT NULL,
  `personal_income_aid_ratio` float DEFAULT NULL,
  `market_value_personal_income_aid_ratio` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `aid_ratio_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ap_general`
--

DROP TABLE IF EXISTS `ap_general`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ap_general` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `promotion_rate_all_students` float DEFAULT NULL,
  `ap_ib_college_credit` float DEFAULT NULL,
  `attendance_rate` float DEFAULT NULL,
  `calculated_score` float DEFAULT NULL,
  `cohort_grad_rate` float DEFAULT NULL,
  `industry_standards_based_competency_assessments_percent` float DEFAULT NULL,
  `percent_industry_standards_based_competency_assessments_advanced` float DEFAULT NULL,
  `final_academic_score` float DEFAULT NULL,
  `percent_3_higher_ap_4_higher_ib` float DEFAULT NULL,
  `grade_12_enrollment` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `ap_general_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ap_percent_gap_met_all`
--

DROP TABLE IF EXISTS `ap_percent_gap_met_all`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ap_percent_gap_met_all` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `math_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `ela_lit_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `science_bio_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `ela_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `bio_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `algebra_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `science_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `math_alg_percent_required_gap_closure_met_all` float DEFAULT NULL,
  `lit_percent_required_gap_closure_met_all` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `ap_percent_gap_met_all_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ap_percent_gap_met_hus`
--

DROP TABLE IF EXISTS `ap_percent_gap_met_hus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ap_percent_gap_met_hus` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `math_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `ela_lit_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `science_bio_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `ela_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `bio_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `algebra_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `science_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `math_alg_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  `lit_percent_required_gap_closure_met_hus` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `ap_percent_gap_met_hus_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ap_pssa_keystone`
--

DROP TABLE IF EXISTS `ap_pssa_keystone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ap_pssa_keystone` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `ela_meeting_annual_academic_growth_expectations` float DEFAULT NULL,
  `ela_percent_proficient_or_advanced_pssa` float DEFAULT NULL,
  `math_meeting_annual_academic_growth_expectations` float DEFAULT NULL,
  `math_percent_proficient_or_advanced_keystone` float DEFAULT NULL,
  `science_bio_meeting_annual_academic_growth_exp` float DEFAULT NULL,
  `science_bio_percent_proficient_advanced_pssa_keystone` float DEFAULT NULL,
  `percent_pssa_keystone_advanced_ela_lit` float DEFAULT NULL,
  `percent_pssa_keystone_advanced_math_alg` float DEFAULT NULL,
  `percent_pssa_keystone_advanced_scnice_bio` float DEFAULT NULL,
  `grade_3_percent_proficient_advanced` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `ap_pssa_keystone_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ap_sat_act`
--

DROP TABLE IF EXISTS `ap_sat_act`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ap_sat_act` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `sat_act_college_ready_benchmark` float DEFAULT NULL,
  `num_grade_12_meeting_benchmarks` int DEFAULT NULL,
  `number_grade_12_with_22_higher_act` int DEFAULT NULL,
  `number_grade_12_with_3_higher_ap_4_higher_ib` int DEFAULT NULL,
  `number_grade_12_taking_plan` int DEFAULT NULL,
  `number_grade_12_taking_psat` int DEFAULT NULL,
  `psat_plan_participation` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `ap_sat_act_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `basic_edu_funding`
--

DROP TABLE IF EXISTS `basic_edu_funding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `basic_edu_funding` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `final_bef` float DEFAULT NULL,
  `base_bef` float DEFAULT NULL,
  `student_weighted_distribution` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `basic_edu_funding_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `county`
--

DROP TABLE IF EXISTS `county`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `county` (
  `county_id` int NOT NULL AUTO_INCREMENT,
  `county_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`county_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `district`
--

DROP TABLE IF EXISTS `district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `district` (
  `district_aun` int NOT NULL,
  `district_name` varchar(100) DEFAULT NULL,
  `county_id` int DEFAULT NULL,
  PRIMARY KEY (`district_aun`),
  KEY `county_id` (`county_id`),
  CONSTRAINT `district_ibfk_1` FOREIGN KEY (`county_id`) REFERENCES `county` (`county_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `district_demographic`
--

DROP TABLE IF EXISTS `district_demographic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `district_demographic` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `per_african_american` float DEFAULT NULL,
  `per_am_indian_or_alaskan_native` float DEFAULT NULL,
  `per_pacific_islander` float DEFAULT NULL,
  `per_two_or_more_races` float DEFAULT NULL,
  `per_white` float DEFAULT NULL,
  `per_hispanic` float DEFAULT NULL,
  `per_asian` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `district_demographic_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `district_fiscal_data`
--

DROP TABLE IF EXISTS `district_fiscal_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `district_fiscal_data` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `average_daily_membership` float DEFAULT NULL,
  `based_on_instruction` float DEFAULT NULL,
  `based_on_total` float DEFAULT NULL,
  `facilities_acquisition_and_construction` float DEFAULT NULL,
  `federal_revenue` float DEFAULT NULL,
  `general_fund_balance` float DEFAULT NULL,
  `local_revenue` float DEFAULT NULL,
  `mv_pi_aid_ratio` float DEFAULT NULL,
  `instruction` float DEFAULT NULL,
  `state_revenue` float DEFAULT NULL,
  `non_instructional` float DEFAULT NULL,
  `other_revenue` float DEFAULT NULL,
  `other_financing_uses` float DEFAULT NULL,
  `supporting_services` float DEFAULT NULL,
  `total_expenditures` float DEFAULT NULL,
  `total_revenues` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `district_fiscal_data_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `district_info`
--

DROP TABLE IF EXISTS `district_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `district_info` (
  `district_aun` int NOT NULL,
  `c_and_t_web` varchar(50) DEFAULT NULL,
  `c_and_t_enrollment` int DEFAULT NULL,
  `c_and_t_name` varchar(100) DEFAULT NULL,
  `IMU_name` varchar(100) DEFAULT NULL,
  `IMU_website` varchar(50) DEFAULT NULL,
  `street_address` varchar(50) DEFAULT NULL,
  `city_address` varchar(25) DEFAULT NULL,
  `zip_code` int DEFAULT NULL,
  `website` varchar(50) DEFAULT NULL,
  `phone_num` varchar(50) DEFAULT NULL,
  `grades_off` varchar(25) DEFAULT NULL,
  `num_schools` int DEFAULT NULL,
  `geographic_size` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`),
  CONSTRAINT `district_info_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `expenditures_general`
--

DROP TABLE IF EXISTS `expenditures_general`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenditures_general` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `current_expenditures` float DEFAULT NULL,
  `other_expenditures` float DEFAULT NULL,
  `actual_instruction_summer` float DEFAULT NULL,
  `instructional_staff` float DEFAULT NULL,
  `administration` float DEFAULT NULL,
  `pupil_health` float DEFAULT NULL,
  `business` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `expenditures_general_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `expenditures_per_adm`
--

DROP TABLE IF EXISTS `expenditures_per_adm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenditures_per_adm` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `adm` float DEFAULT NULL,
  `weighted_adm` float DEFAULT NULL,
  `instruction_per_adm` float DEFAULT NULL,
  `support_services_per_adm` float DEFAULT NULL,
  `non_instructional_per_adm` float DEFAULT NULL,
  `current_exp_per_adm` float DEFAULT NULL,
  `facilities_construction_per_adm` float DEFAULT NULL,
  `other_financing_uses_per_adm` float DEFAULT NULL,
  `total_exp_per_adm` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `expenditures_per_adm_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `expenditures_programs`
--

DROP TABLE IF EXISTS `expenditures_programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenditures_programs` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `regular_programs` float DEFAULT NULL,
  `special_programs` float DEFAULT NULL,
  `vocational_programs` float DEFAULT NULL,
  `other_institutional_programs` float DEFAULT NULL,
  `non_public_programs` float DEFAULT NULL,
  `adult_education_programs` float DEFAULT NULL,
  `higher_education_programs` float DEFAULT NULL,
  `higher_ed_programs_secondary` float DEFAULT NULL,
  `pre_kindergarten` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `expenditures_programs_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `expenditures_services`
--

DROP TABLE IF EXISTS `expenditures_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenditures_services` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `instruction` float DEFAULT NULL,
  `support_services` float DEFAULT NULL,
  `noninstructional_services` float DEFAULT NULL,
  `improvement_services` float DEFAULT NULL,
  `support_services_students` float DEFAULT NULL,
  `operation_of_plant_services` float DEFAULT NULL,
  `students_transportation_services` float DEFAULT NULL,
  `central` float DEFAULT NULL,
  `other_support_services` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `expenditures_services_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `extra_demo_district`
--

DROP TABLE IF EXISTS `extra_demo_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `extra_demo_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `per_military_connected` float DEFAULT NULL,
  `per_gifted_student` float DEFAULT NULL,
  `per_special_education` float DEFAULT NULL,
  `per_english_learner` float DEFAULT NULL,
  `per_foster_care` float DEFAULT NULL,
  `per_homeless` float DEFAULT NULL,
  `per_economically_disadvantaged` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `extra_demo_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `extra_demo_school`
--

DROP TABLE IF EXISTS `extra_demo_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `extra_demo_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `per_english_learner` float DEFAULT NULL,
  `per_special_education` float DEFAULT NULL,
  `per_gifted_student` float DEFAULT NULL,
  `per_military_connected` float DEFAULT NULL,
  `per_foster_care` float DEFAULT NULL,
  `per_economiccaly_disadvantaged` float DEFAULT NULL,
  `per_homeless` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `extra_demo_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gender_district`
--

DROP TABLE IF EXISTS `gender_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gender_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `male` float DEFAULT NULL,
  `female` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `gender_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gender_school`
--

DROP TABLE IF EXISTS `gender_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gender_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `male` float DEFAULT NULL,
  `female` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `gender_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `grad_rate_by_category_district`
--

DROP TABLE IF EXISTS `grad_rate_by_category_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grad_rate_by_category_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `x_year_cohort` int DEFAULT NULL,
  `cohort_grad_rate` float DEFAULT NULL,
  `male_grad_rate` float DEFAULT NULL,
  `female_grad_rate` float DEFAULT NULL,
  `special_ed_grad_rate` float DEFAULT NULL,
  `el_grad_rate` float DEFAULT NULL,
  `econ_disadvantaged_grad_rate` float DEFAULT NULL,
  `migrant_grad_rate` float DEFAULT NULL,
  `foster_grad_rate` float DEFAULT NULL,
  `homeless_grad_rate` float DEFAULT NULL,
  `military_grad_rate` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `grad_rate_by_category_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `grad_rate_by_category_school`
--

DROP TABLE IF EXISTS `grad_rate_by_category_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grad_rate_by_category_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `x_year_cohort` int DEFAULT NULL,
  `cohort_grad_rate` float DEFAULT NULL,
  `male_grad_rate` float DEFAULT NULL,
  `female_grad_rate` float DEFAULT NULL,
  `special_ed_grad_rate` float DEFAULT NULL,
  `el_grad_rate` float DEFAULT NULL,
  `econ_disadvantaged_grad_rate` float DEFAULT NULL,
  `migrant_grad_rate` float DEFAULT NULL,
  `foster_grad_rate` float DEFAULT NULL,
  `homeless_grad_rate` float DEFAULT NULL,
  `military_grad_rate` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `grad_rate_by_category_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `grad_rate_by_race_district`
--

DROP TABLE IF EXISTS `grad_rate_by_race_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grad_rate_by_race_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `x_year_cohort` int DEFAULT NULL,
  `aian_grad_rate` float DEFAULT NULL,
  `native_hawaiin_pacific_islander_grad_rate` float DEFAULT NULL,
  `asian_grad_rate` float DEFAULT NULL,
  `black_grad_rate` float DEFAULT NULL,
  `hispanic_grad_rate` float DEFAULT NULL,
  `white_grad_rate` float DEFAULT NULL,
  `multi_racial_grad_rate` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `grad_rate_by_race_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `grad_rate_by_race_school`
--

DROP TABLE IF EXISTS `grad_rate_by_race_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grad_rate_by_race_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `x_year_cohort` int DEFAULT NULL,
  `aian_grad_rate` float DEFAULT NULL,
  `native_hawaiin_pacific_islander_grad_rate` float DEFAULT NULL,
  `asian_grad_rate` float DEFAULT NULL,
  `black_grad_rate` float DEFAULT NULL,
  `hispanic_grad_rate` float DEFAULT NULL,
  `white_grad_rate` float DEFAULT NULL,
  `multi_racial_grad_rate` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `grad_rate_by_race_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `keystone_grade_school`
--

DROP TABLE IF EXISTS `keystone_grade_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `keystone_grade_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `keystone_subject` varchar(25) DEFAULT NULL,
  `student_group` varchar(75) DEFAULT NULL,
  `grade` int DEFAULT NULL,
  `number_scored` int DEFAULT NULL,
  `percent_advanced` float DEFAULT NULL,
  `percent_proficient` float DEFAULT NULL,
  `percent_basic` float DEFAULT NULL,
  `percent_below_basic` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `keystone_grade_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `low_income_percent_district`
--

DROP TABLE IF EXISTS `low_income_percent_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `low_income_percent_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `total_enrollment` int DEFAULT NULL,
  `low_income_enrollment` int DEFAULT NULL,
  `percent_of_enrollment_from_low_income_families` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `low_income_percent_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `low_income_percent_private_school`
--

DROP TABLE IF EXISTS `low_income_percent_private_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `low_income_percent_private_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `low_income_percentage` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `low_income_percent_private_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `low_income_percent_pub_school`
--

DROP TABLE IF EXISTS `low_income_percent_pub_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `low_income_percent_pub_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `total_enrollment` int DEFAULT NULL,
  `low_income_enrollment` int DEFAULT NULL,
  `percent_enrollment_from_low_income_families` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `low_income_percent_pub_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `misc`
--

DROP TABLE IF EXISTS `misc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misc` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `mv_pi_aid_ratio` float DEFAULT NULL,
  `adm` float DEFAULT NULL,
  `wadm` float DEFAULT NULL,
  `eq_mills` float DEFAULT NULL,
  `pop_per_sq_mile` float DEFAULT NULL,
  `aie_per_wadm` float DEFAULT NULL,
  `total_exp_per_adm` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `misc_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `misc_rank`
--

DROP TABLE IF EXISTS `misc_rank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misc_rank` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `mv_pi_rk` int DEFAULT NULL,
  `wadm_rk` int DEFAULT NULL,
  `eq_mills_rk` int DEFAULT NULL,
  `pop_per_sq_mile_rk` int DEFAULT NULL,
  `aie_per_wadm_rk` int DEFAULT NULL,
  `total_exp_per_adm_rk` int DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `misc_rank_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `personal_income`
--

DROP TABLE IF EXISTS `personal_income`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_income` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `records` int DEFAULT NULL,
  `compensation` float DEFAULT NULL,
  `net_profits` float DEFAULT NULL,
  `dividends_and_interest` float DEFAULT NULL,
  `misc_income` float DEFAULT NULL,
  `out_of_st_tax_records` int DEFAULT NULL,
  `out_of_st_tax_credit` float DEFAULT NULL,
  `out_of_st_income` float DEFAULT NULL,
  `total_personal_income` float DEFAULT NULL,
  `adjusted_personal_income` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `personal_income_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_elem_enrollment_fully_public_paid`
--

DROP TABLE IF EXISTS `private_non_public_elem_enrollment_fully_public_paid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_elem_enrollment_fully_public_paid` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `k4` int DEFAULT NULL,
  `k5` int DEFAULT NULL,
  `grade_1` int DEFAULT NULL,
  `grade_2` int DEFAULT NULL,
  `grade_3` int DEFAULT NULL,
  `grade_4` int DEFAULT NULL,
  `grade_5` int DEFAULT NULL,
  `grade_6` int DEFAULT NULL,
  `grade_7E` int DEFAULT NULL,
  `grade_8E` int DEFAULT NULL,
  `total_elementary_ungraded` int DEFAULT NULL,
  `non_resident` int DEFAULT NULL,
  `resident` int DEFAULT NULL,
  `total_elementary_enrollment` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_elem_enrollment_fully_public_paid_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_elem_enrollment_private_paid`
--

DROP TABLE IF EXISTS `private_non_public_elem_enrollment_private_paid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_elem_enrollment_private_paid` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `k4` int DEFAULT NULL,
  `k5` int DEFAULT NULL,
  `grade_1` int DEFAULT NULL,
  `grade_2` int DEFAULT NULL,
  `grade_3` int DEFAULT NULL,
  `grade_4` int DEFAULT NULL,
  `grade_5` int DEFAULT NULL,
  `grade_6` int DEFAULT NULL,
  `grade_7E` int DEFAULT NULL,
  `grade_8E` int DEFAULT NULL,
  `total_elementary_ungraded` int DEFAULT NULL,
  `non_resident` int DEFAULT NULL,
  `resident` int DEFAULT NULL,
  `total_elementary_enrollment` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_elem_enrollment_private_paid_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_full_time_equivalent_teachers`
--

DROP TABLE IF EXISTS `private_non_public_full_time_equivalent_teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_full_time_equivalent_teachers` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `nursery_fte` float DEFAULT NULL,
  `elementary_fte` float DEFAULT NULL,
  `secondary_fte` float DEFAULT NULL,
  `special_education_fte` float DEFAULT NULL,
  `total_fte` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_full_time_equivalent_teachers_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_low_income_enrollment`
--

DROP TABLE IF EXISTS `private_non_public_low_income_enrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_low_income_enrollment` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `percent_nursery_low_income` float DEFAULT NULL,
  `percent_k12_low_income` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_low_income_enrollment_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_other_enrollment_private_paid`
--

DROP TABLE IF EXISTS `private_non_public_other_enrollment_private_paid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_other_enrollment_private_paid` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `nursery` int DEFAULT NULL,
  `special_ed_preschool_k5` int DEFAULT NULL,
  `special_ed_preschool_nursery_age_3_4_5` int DEFAULT NULL,
  `non_resident` int DEFAULT NULL,
  `resident` int DEFAULT NULL,
  `total_other_enrollment` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_other_enrollment_private_paid_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_other_enrollment_public_paid`
--

DROP TABLE IF EXISTS `private_non_public_other_enrollment_public_paid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_other_enrollment_public_paid` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `nursery` int DEFAULT NULL,
  `special_ed_preschool_k5` int DEFAULT NULL,
  `special_ed_preschool_nursery_age_3_4_5` int DEFAULT NULL,
  `non_resident` int DEFAULT NULL,
  `resident` int DEFAULT NULL,
  `total_other_enrollment` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_other_enrollment_public_paid_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_secondary_enrollment_fully_public_paid`
--

DROP TABLE IF EXISTS `private_non_public_secondary_enrollment_fully_public_paid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_secondary_enrollment_fully_public_paid` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `grade_9` int DEFAULT NULL,
  `grade_10` int DEFAULT NULL,
  `grade_11` int DEFAULT NULL,
  `grade_12` int DEFAULT NULL,
  `secondary_ungraded` int DEFAULT NULL,
  `non_resident` int DEFAULT NULL,
  `resident` int DEFAULT NULL,
  `total_secondary_enrollment` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_secondary_enrollment_fully_public_paid_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_secondary_enrollment_private_paid`
--

DROP TABLE IF EXISTS `private_non_public_secondary_enrollment_private_paid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_secondary_enrollment_private_paid` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `grade_9` int DEFAULT NULL,
  `grade_10` int DEFAULT NULL,
  `grade_11` int DEFAULT NULL,
  `grade_12` int DEFAULT NULL,
  `secondary_ungraded` int DEFAULT NULL,
  `non_resident` int DEFAULT NULL,
  `resident` int DEFAULT NULL,
  `total_secondary_enrollment` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_secondary_enrollment_private_paid_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_non_public_total`
--

DROP TABLE IF EXISTS `private_non_public_total`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_non_public_total` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `grand_total` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `private_non_public_total_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pssa_school`
--

DROP TABLE IF EXISTS `pssa_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pssa_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `pssa_subject` varchar(100) DEFAULT NULL,
  `group_students` varchar(75) DEFAULT NULL,
  `grade` int DEFAULT NULL,
  `number_scored` float DEFAULT NULL,
  `percent_advanced` float DEFAULT NULL,
  `percent_proficient` float DEFAULT NULL,
  `percent_basic` float DEFAULT NULL,
  `percent_below_basic` float DEFAULT NULL,
  `percent_proficient_and_above` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `pssa_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `public_school_dropouts_district`
--

DROP TABLE IF EXISTS `public_school_dropouts_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public_school_dropouts_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `oct_1_enrollment_grades_7_12` int DEFAULT NULL,
  `male_dropouts` int DEFAULT NULL,
  `female_dropouts` int DEFAULT NULL,
  `dropouts` int DEFAULT NULL,
  `dropout_rate` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `public_school_dropouts_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `public_school_dropouts_school`
--

DROP TABLE IF EXISTS `public_school_dropouts_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public_school_dropouts_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `oct_1_enrollment_grades_7_12` int DEFAULT NULL,
  `male_dropouts` int DEFAULT NULL,
  `female_dropouts` int DEFAULT NULL,
  `dropouts` int DEFAULT NULL,
  `dropout_rate` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `public_school_dropouts_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `public_school_enrollment_district`
--

DROP TABLE IF EXISTS `public_school_enrollment_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public_school_enrollment_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `pka` int DEFAULT NULL,
  `pkp` int DEFAULT NULL,
  `pkf` int DEFAULT NULL,
  `k4a` int DEFAULT NULL,
  `k4p` int DEFAULT NULL,
  `k4f` int DEFAULT NULL,
  `k5a` int DEFAULT NULL,
  `k5p` int DEFAULT NULL,
  `k5f` int DEFAULT NULL,
  `grade_1` int DEFAULT NULL,
  `grade_2` int DEFAULT NULL,
  `grade_3` int DEFAULT NULL,
  `grade_4` int DEFAULT NULL,
  `grade_5` int DEFAULT NULL,
  `grade_6` int DEFAULT NULL,
  `grade_7` int DEFAULT NULL,
  `grade_8` int DEFAULT NULL,
  `grade_9` int DEFAULT NULL,
  `grade_10` int DEFAULT NULL,
  `grade_11` int DEFAULT NULL,
  `grade_12` int DEFAULT NULL,
  `total` int DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `public_school_enrollment_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `public_school_enrollment_school`
--

DROP TABLE IF EXISTS `public_school_enrollment_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public_school_enrollment_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `pka` int DEFAULT NULL,
  `pkp` int DEFAULT NULL,
  `pkf` int DEFAULT NULL,
  `k4a` int DEFAULT NULL,
  `k4p` int DEFAULT NULL,
  `k4f` int DEFAULT NULL,
  `k5a` int DEFAULT NULL,
  `k5p` int DEFAULT NULL,
  `k5f` int DEFAULT NULL,
  `grade_1` int DEFAULT NULL,
  `grade_2` int DEFAULT NULL,
  `grade_3` int DEFAULT NULL,
  `grade_4` int DEFAULT NULL,
  `grade_5` int DEFAULT NULL,
  `grade_6` int DEFAULT NULL,
  `grade_7` int DEFAULT NULL,
  `grade_8` int DEFAULT NULL,
  `grade_9` int DEFAULT NULL,
  `grade_10` int DEFAULT NULL,
  `grade_11` int DEFAULT NULL,
  `grade_12` int DEFAULT NULL,
  `total` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `public_school_enrollment_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `public_school_grad_rates_district`
--

DROP TABLE IF EXISTS `public_school_grad_rates_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public_school_grad_rates_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `total_graduates` int DEFAULT NULL,
  `total_college_bound` int DEFAULT NULL,
  `total_college_bound_percentage` float DEFAULT NULL,
  `two_four_year_college_university` int DEFAULT NULL,
  `two_four_year_college_university_percentage` float DEFAULT NULL,
  `total_postsecondary_bound` int DEFAULT NULL,
  `total_postsecondary_bound_percentage` float DEFAULT NULL,
  `non_degree_getting_postsecondary_school` int DEFAULT NULL,
  `non_degree_getting_postsecondary_school_percentage` float DEFAULT NULL,
  `specialized_associate_degree_getting_institution` int DEFAULT NULL,
  `specialized_associate_degree_getting_institution_percentage` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `public_school_grad_rates_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `public_school_grad_rates_school`
--

DROP TABLE IF EXISTS `public_school_grad_rates_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public_school_grad_rates_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `total_graduates` int DEFAULT NULL,
  `total_college_bound` int DEFAULT NULL,
  `total_college_bound_percentage` float DEFAULT NULL,
  `two_four_year_college_university` int DEFAULT NULL,
  `two_four_year_college_university_percentage` float DEFAULT NULL,
  `total_postsecondary_bound` int DEFAULT NULL,
  `total_postsecondary_bound_percentage` float DEFAULT NULL,
  `non_degree_getting_postsecondary_school` int DEFAULT NULL,
  `non_degree_getting_postsecondary_school_percentage` float DEFAULT NULL,
  `specialized_associate_degree_getting_institution` int DEFAULT NULL,
  `specialized_associate_degree_getting_institution_percentage` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `public_school_grad_rates_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `real_estate_tax`
--

DROP TABLE IF EXISTS `real_estate_tax`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `real_estate_tax` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `municipality_and_other` varchar(100) DEFAULT NULL,
  `real_estate_mills` float DEFAULT NULL,
  `additional_community_college_mills` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `real_estate_tax_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `revenues_by_source`
--

DROP TABLE IF EXISTS `revenues_by_source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `revenues_by_source` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `total_revenue` float DEFAULT NULL,
  `local_taxes` float DEFAULT NULL,
  `local_other` float DEFAULT NULL,
  `total_local_revenue` float DEFAULT NULL,
  `local_per_of_total_revenue` float DEFAULT NULL,
  `total_state_revenue` float DEFAULT NULL,
  `state_per_of_total_revenue` float DEFAULT NULL,
  `revenue_from_federal_sources` float DEFAULT NULL,
  `federal_per_of_total_revenue` float DEFAULT NULL,
  `total_other_revenue` float DEFAULT NULL,
  `other_per_of_total_revenue` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `revenues_by_source_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `revenues_per_adm`
--

DROP TABLE IF EXISTS `revenues_per_adm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `revenues_per_adm` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `adm` float DEFAULT NULL,
  `total_revenue_per_adm` float DEFAULT NULL,
  `total_rank_total` int DEFAULT NULL,
  `local_revenue_per_adm` float DEFAULT NULL,
  `total_rank_local` int DEFAULT NULL,
  `state_revenue_per_adm` float DEFAULT NULL,
  `total_rank_state` int DEFAULT NULL,
  `federal_revenue_per_adm` float DEFAULT NULL,
  `total_rank_federal` int DEFAULT NULL,
  `other_revenue_per_adm` float DEFAULT NULL,
  `total_rank_other` int DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `revenues_per_adm_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `revenues_taxes_coll`
--

DROP TABLE IF EXISTS `revenues_taxes_coll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `revenues_taxes_coll` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `total_taxes_collected` float DEFAULT NULL,
  `real_estate_taxes_collected` float DEFAULT NULL,
  `public_utility_realty_taxes_collected` float DEFAULT NULL,
  `payment_in_lieu_taxes_collected` float DEFAULT NULL,
  `per_capita_taxes_collected` float DEFAULT NULL,
  `first_class_sd_taxes_collected` float DEFAULT NULL,
  `delinquent_taxes_collected` float DEFAULT NULL,
  `steb_market_value` float DEFAULT NULL,
  `equalized_mills` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `revenues_taxes_coll_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school` (
  `school_id` int NOT NULL,
  `school_name` varchar(100) DEFAULT NULL,
  `district_aun` int DEFAULT NULL,
  PRIMARY KEY (`school_id`),
  KEY `district_aun` (`district_aun`),
  CONSTRAINT `school_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `school_demographic`
--

DROP TABLE IF EXISTS `school_demographic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school_demographic` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `per_asian` float DEFAULT NULL,
  `per_hispanic` float DEFAULT NULL,
  `per_pacific_islander` float DEFAULT NULL,
  `per_am_indian_or_alaskan_native` float DEFAULT NULL,
  `per_african_american` float DEFAULT NULL,
  `per_white` float DEFAULT NULL,
  `per_two_or_more_races` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `school_demographic_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `school_fiscal_data`
--

DROP TABLE IF EXISTS `school_fiscal_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school_fiscal_data` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `state_personnel` float DEFAULT NULL,
  `state_non_personnel` float DEFAULT NULL,
  `local_personnel` float DEFAULT NULL,
  `local_non_personnel` float DEFAULT NULL,
  `federal_personnel` float DEFAULT NULL,
  `federal_non_personnel` float DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `school_fiscal_data_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `school_info`
--

DROP TABLE IF EXISTS `school_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school_info` (
  `school_id` int NOT NULL,
  `street_address` varchar(50) DEFAULT NULL,
  `city_address` varchar(25) DEFAULT NULL,
  `zip_code` int DEFAULT NULL,
  `website` varchar(50) DEFAULT NULL,
  `phone_num` varchar(25) DEFAULT NULL,
  `grades_off` varchar(25) DEFAULT NULL,
  `title_1` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`school_id`),
  CONSTRAINT `school_info_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sec_career_technical_fund`
--

DROP TABLE IF EXISTS `sec_career_technical_fund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sec_career_technical_fund` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `final_sctes` float DEFAULT NULL,
  `aie_per_wadm` float DEFAULT NULL,
  `ber` float DEFAULT NULL,
  `vocational_adm` float DEFAULT NULL,
  `voc_adm_multiplier` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `sec_career_technical_fund_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `special_edu_funding`
--

DROP TABLE IF EXISTS `special_edu_funding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `special_edu_funding` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `final_sef` float DEFAULT NULL,
  `base_sef` float DEFAULT NULL,
  `student_based_allocation` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `special_edu_funding_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `total_grads_district`
--

DROP TABLE IF EXISTS `total_grads_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `total_grads_district` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `x_year_cohort` int DEFAULT NULL,
  `grads` int DEFAULT NULL,
  `cohort` int DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `total_grads_district_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `total_grads_school`
--

DROP TABLE IF EXISTS `total_grads_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `total_grads_school` (
  `school_id` int NOT NULL,
  `school_year` int NOT NULL,
  `x_year_cohort` int DEFAULT NULL,
  `grads` int DEFAULT NULL,
  `cohort` int DEFAULT NULL,
  PRIMARY KEY (`school_id`,`school_year`),
  CONSTRAINT `total_grads_school_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `school` (`school_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `wadm_grades`
--

DROP TABLE IF EXISTS `wadm_grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wadm_grades` (
  `district_aun` int NOT NULL,
  `school_year` int NOT NULL,
  `wadm_pre_kindergarten_ht` float DEFAULT NULL,
  `wadm_pre_kindergarten_ft` float DEFAULT NULL,
  `wadm_kindergarten_ht4` float DEFAULT NULL,
  `wadm_kindergarten_ft4` float DEFAULT NULL,
  `wadm_kindergarten_ht5` float DEFAULT NULL,
  `wadm_kindergarten_ft5` float DEFAULT NULL,
  `wadm_elementary` float DEFAULT NULL,
  `wadm_secondary` float DEFAULT NULL,
  `adjustment_factor` float DEFAULT NULL,
  PRIMARY KEY (`district_aun`,`school_year`),
  CONSTRAINT `wadm_grades_ibfk_1` FOREIGN KEY (`district_aun`) REFERENCES `district` (`district_aun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-10 17:30:46
