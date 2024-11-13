CREATE SCHEMA dbms_proj;
USE dbms_proj;

CREATE TABLE county(
	county_id INT PRIMARY KEY AUTO_INCREMENT,
    county_name VARCHAR(100)
);

CREATE TABLE district(
	district_aun INT PRIMARY KEY,
    district_name VARCHAR(100),
    county_id INT,
    FOREIGN KEY (county_id) REFERENCES county(county_id)
);

CREATE TABLE school(
	school_id INT PRIMARY KEY,
    school_name VARCHAR(100),
    district_aun INT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun)
);

CREATE TABLE school_info(
	school_id INT PRIMARY KEY,
    street_address VARCHAR(50),
    city_address VARCHAR(25),
    zip_code INT,
    website VARCHAR(50),
    phone_num VARCHAR(25),
    grades_off VARCHAR(25),
    title_1 BOOLEAN,
    FOREIGN KEY (school_id) REFERENCES school(school_id)
);

CREATE TABLE gender_school(
	school_id INT,
    school_year INT,
    male FLOAT,
    female FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_gender_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE school_demographic(
	school_id INT,
    school_year INT,
    per_asian FLOAT,
    per_hispanic FLOAT,
    per_pacific_islander FLOAT,
    per_am_indian_or_alaskan_native FLOAT,
    per_african_american FLOAT,
    per_white FLOAT,
    per_two_or_more_races FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_school_demographic PRIMARY KEY (school_id, school_year)
);

CREATE TABLE extra_demo_school(
	school_id INT,
    school_year INT,
    per_english_learner FLOAT,
    per_special_education FLOAT,
    per_gifted_student FLOAT,
    per_military_connected FLOAT,
    per_foster_care FLOAT,
    per_economiccaly_disadvantaged FLOAT,
    per_homeless FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_extra_demo_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE gender_district(
	district_aun INT,
    school_year INT,
    male FLOAT,
    female FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_gender_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE district_demographic(
	district_aun INT,
    school_year INT,
    per_african_american FLOAT,
    per_am_indian_or_alaskan_native FLOAT,
    per_pacific_islander FLOAT,
    per_two_or_more_races FLOAT,
    per_white FLOAT,
    per_hispanic FLOAT,
    per_asian FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_district_demographic PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE extra_demo_district(
	district_aun INT,
    school_year INT,
    per_military_connected FLOAT,
    per_gifted_student FLOAT,
    per_special_education FLOAT,
    per_english_learner FLOAT,
    per_foster_care FLOAT,
    per_homeless FLOAT,
    per_economically_disadvantaged FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_extra_demo_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE district_info(
	district_aun INT PRIMARY KEY,
    c_and_t_web VARCHAR(50),
    c_and_t_enrollment INT,
    c_and_t_name VARCHAR(100),
    IMU_name varchar(100),
    IMU_website varchar(50),
    street_address varchar(50),
    city_address varchar(25),
    zip_code INT,
    website varchar(50),
    phone_num VARCHAR(50),
    grades_off VARCHAR(25),
    num_schools INT,
    geographic_size FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun)
);

CREATE TABLE school_fiscal_data(
	school_id INT,
    school_year INT,
    state_personnel FLOAT,
    state_non_personnel FLOAT,
    local_personnel FLOAT,
    local_non_personnel FLOAT,
    federal_personnel FLOAT,
    federal_non_personnel FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_school_fiscal_data PRIMARY KEY (school_id, school_year)
);

CREATE TABLE district_fiscal_data(
	district_aun INT,
    school_year INT,
    average_daily_membership FLOAT,
    based_on_instruction FLOAT,
    based_on_total FLOAT,
    facilities_acquisition_and_construction FLOAT,
    federal_revenue FLOAT,
    general_fund_balance FLOAT,
    local_revenue FLOAT,
    mv_pi_aid_ratio FLOAT,
    instruction FLOAT,
    state_revenue FLOAT,
    non_instructional FLOAT,
    other_revenue FLOAT,
    other_financing_uses FLOAT,
    supporting_services FLOAT,
    total_expenditures FLOAT,
    total_revenues FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_district_fiscal_data PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE expenditures_general(
	district_aun INT,
    school_year INT,
    current_expenditures FLOAT,
    other_expenditures FLOAT,
    actual_instruction_summer FLOAT,
    instructional_staff FLOAT,
    administration FLOAT,
    pupil_health FLOAT,
    business FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_expenditures_general PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE expenditures_programs(
	district_aun INT,
    school_year INT,
    regular_programs FLOAT,
    special_programs FLOAT,
    vocational_programs FLOAT,
    other_institutional_programs FLOAT,
    non_public_programs FLOAT,
    adult_education_programs FLOAT,
    higher_education_programs FLOAT,
    higher_ed_programs_secondary FLOAT,
    pre_kindergarten FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_expenditures_programs PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE expenditures_services(
	district_aun INT,
    school_year INT,
    instruction FLOAT,
    support_services FLOAT,
    noninstructional_services FLOAT,
    improvement_services FLOAT,
    support_services_students FLOAT,
    operation_of_plant_services FLOAT,
    students_transportation_services FLOAT,
    central FLOAT,
    other_support_services FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_expenditures_services PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE expenditures_per_adm(
	district_aun INT,
    school_year INT,
    adm FLOAT,
    weighted_adm FLOAT,
    instruction_per_adm FLOAT,
    support_services_per_adm FLOAT,
    non_instructional_per_adm FLOAT,
    current_exp_per_adm FLOAT,
    facilities_construction_per_adm FLOAT,
    other_financing_uses_per_adm FLOAT,
    total_exp_per_adm FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_expenditures_per_adm PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE revenues_by_source(
	district_aun INT,
    school_year INT,
    total_revenue FLOAT,
    local_taxes FLOAT,
    local_other FLOAT,
    total_local_revenue FLOAT,
    local_per_of_total_revenue FLOAT,
    total_state_revenue FLOAT,
    state_per_of_total_revenue FLOAT,
    revenue_from_federal_sources FLOAT,
    federal_per_of_total_revenue FLOAT,
    total_other_revenue FLOAT,
    other_per_of_total_revenue FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_revenues_by_source PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE revenues_per_adm(
	district_aun INT,
    school_year INT,
    adm FLOAT,
    total_revenue_per_adm FLOAT,
    total_rank_total INT,
    local_revenue_per_adm FLOAT,
    total_rank_local INT,
    state_revenue_per_adm FLOAT,
    total_rank_state INT,
    federal_revenue_per_adm FLOAT,
    total_rank_federal INT,
    other_revenue_per_adm FLOAT,
    total_rank_other INT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_revenues_per_adm PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE revenues_taxes_coll(
	district_aun INT,
    school_year INT,
    total_taxes_collected FLOAT,
    real_estate_taxes_collected FLOAT,
    public_utility_realty_taxes_collected FLOAT,
    payment_in_lieu_taxes_collected FLOAT,
    per_capita_taxes_collected FLOAT,
    first_class_sd_taxes_collected FLOAT,
    delinquent_taxes_collected FLOAT,
    steb_market_value FLOAT,
    equalized_mills FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_revenues_taxes_coll PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE aid_ratio(
	district_aun INT,
    school_year INT,
    market_value FLOAT,
    personal_income FLOAT,
    wadm FLOAT,
    mv_per_wadm FLOAT,
    market_value_aid_ratio FLOAT,
    pi_per_wadm FLOAT,
    personal_income_aid_ratio FLOAT,
    market_value_personal_income_aid_ratio FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_aid_ratio PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE adm_general(
	district_aun INT,
    school_year INT,
    adm float,
    wadm FLOAT,
    adjusted_adm FLOAT,
    adm_pde_363 FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_adm_general PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE adm_grades(
	district_aun INT,
    school_year INT,
    adm_pre_kindergarten_ht FLOAT,
    adm_pre_kindergarten_ft FLOAT,
    adm_kindergarten_ht4 FLOAT,
    adm_kindergarten_ft4 FLOAT,
    adm_kindergarten_ht5 FLOAT,
    adm_kindergarten_ft5 FLOAT,
    adm_elementary FLOAT,
    adm_secondary FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_adm_grades PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE wadm_grades(
	district_aun INT,
    school_year INT,
    wadm_pre_kindergarten_ht FLOAT,
    wadm_pre_kindergarten_ft FLOAT,
    wadm_kindergarten_ht4 FLOAT,
    wadm_kindergarten_ft4 FLOAT,
    wadm_kindergarten_ht5 FLOAT,
    wadm_kindergarten_ft5 FLOAT,
    wadm_elementary FLOAT,
    wadm_secondary FLOAT,
    adjustment_factor FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_wadm_grades PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE misc(
	district_aun INT,
    school_year INT,
	mv_pi_aid_ratio FLOAT,
    adm FLOAT,
    wadm FLOAT,
    eq_mills FLOAT,
    pop_per_sq_mile FLOAT,
    aie_per_wadm FLOAT,
    total_exp_per_adm FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_misc PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE misc_rank(
	district_aun INT,
    school_year INT,
	mv_pi_rk INT,
    wadm_rk INT,
    eq_mills_rk INT,
    pop_per_sq_mile_rk INT,
    aie_per_wadm_rk INT,
    total_exp_per_adm_rk INT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_misc_rank PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE personal_income(
	district_aun INT,
    school_year INT,
	records INT,
    compensation FLOAT,
    net_profits FLOAT,
    dividends_and_interest FLOAT,
    misc_income FLOAT,
    out_of_st_tax_records INT,
    out_of_st_tax_credit FLOAT,
    out_of_st_income FLOAT,
    total_personal_income FLOAT,
    adjusted_personal_income FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_personal_income PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE real_estate_tax(
	district_aun INT,
    school_year INT,
	municipality_and_other VARCHAR(100),
    real_estate_mills FLOAT,
    additional_community_college_mills FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_real_estate_tax PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE basic_edu_funding(
	district_aun INT,
    school_year INT,
	final_bef FLOAT,
    base_bef FLOAT,
    student_weighted_distribution FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_basic_edu_funding PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE sec_career_technical_fund(
	district_aun INT,
    school_year INT,
    final_sctes FLOAT,
    aie_per_wadm FLOAT,
    ber FLOAT,
    vocational_adm FLOAT,
    voc_adm_multiplier FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_sec_career_technical_fund PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE special_edu_funding(
	district_aun INT,
    school_year INT,
    final_sef FLOAT,
    base_sef FLOAT,
    student_based_allocation FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_special_edu_funding PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE low_income_percent_pub_school(
	school_id INT,
    school_year INT,
    total_enrollment INT,
    low_income_enrollment INT,
    percent_enrollment_from_low_income_families FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_low_income_percent_pub_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE low_income_percent_district(
	district_aun INT,
    school_year INT,
    total_enrollment INT,
    low_income_enrollment INT,
    percent_of_enrollment_from_low_income_families FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_low_income_percent_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE low_income_percent_private_school(
	school_id INT,
    school_year INT,
    low_income_percentage FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_low_income_percent_private_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE pssa_school(
	school_id INT,
    school_year INT,
    pssa_subject VARCHAR(100),
    group_students VARCHAR(75),
    grade INT,
    number_scored FLOAT,
    percent_advanced FLOAT,
    percent_proficient FLOAT,
    percent_basic FLOAT,
    percent_below_basic FLOAT,
    percent_proficient_and_above FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_pssa_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE ap_percent_gap_met_all(
	school_id INT,
    school_year INT,
    math_percent_required_gap_closure_met_all FLOAT,
    ela_lit_percent_required_gap_closure_met_all FLOAT,
    science_bio_percent_required_gap_closure_met_all FLOAT,
    ela_percent_required_gap_closure_met_all FLOAT,
    bio_percent_required_gap_closure_met_all FLOAT,
    algebra_percent_required_gap_closure_met_all FLOAT,
    science_percent_required_gap_closure_met_all FLOAT,
    math_alg_percent_required_gap_closure_met_all FLOAT,
    lit_percent_required_gap_closure_met_all FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_ap_percent_gap_met_all PRIMARY KEY (school_id, school_year)
);

CREATE TABLE ap_percent_gap_met_hus(
	school_id INT,
    school_year INT,
    math_percent_required_gap_closure_met_hus FLOAT,
    ela_lit_percent_required_gap_closure_met_hus FLOAT,
    science_bio_percent_required_gap_closure_met_hus FLOAT,
    ela_percent_required_gap_closure_met_hus FLOAT,
    bio_percent_required_gap_closure_met_hus FLOAT,
    algebra_percent_required_gap_closure_met_hus FLOAT,
    science_percent_required_gap_closure_met_hus FLOAT,
    math_alg_percent_required_gap_closure_met_hus FLOAT,
    lit_percent_required_gap_closure_met_hus FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_ap_percent_gap_met_hus PRIMARY KEY (school_id, school_year)
);

CREATE TABLE ap_general(
	school_id INT,
    school_year INT,
    promotion_rate_all_students FLOAT,
    ap_ib_college_credit FLOAT,
    attendance_rate FLOAT,
    calculated_score FLOAT,
    cohort_grad_rate FLOAT,
    industry_standards_based_competency_assessments_percent FLOAT,
    percent_industry_standards_based_competency_assessments_advanced FLOAT,
    final_academic_score FLOAT,
    percent_3_higher_ap_4_higher_ib FLOAT,
    grade_12_enrollment INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_ap_general PRIMARY KEY (school_id, school_year)
);

CREATE TABLE ap_pssa_keystone(
	school_id INT,
    school_year INT,
    ela_meeting_annual_academic_growth_expectations FLOAT,
    ela_percent_proficient_or_advanced_pssa FLOAT,
    math_meeting_annual_academic_growth_expectations FLOAT,
    math_percent_proficient_or_advanced_keystone FLOAT,
    science_bio_meeting_annual_academic_growth_exp FLOAT,
    science_bio_percent_proficient_advanced_pssa_keystone FLOAT,
    percent_pssa_keystone_advanced_ela_lit FLOAT,
    percent_pssa_keystone_advanced_math_alg FLOAT,
    percent_pssa_keystone_advanced_scnice_bio FLOAT,
    grade_3_percent_proficient_advanced FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_ap_pssa_keystone PRIMARY KEY (school_id, school_year)
);

CREATE TABLE ap_sat_act(
	school_id INT,
    school_year INT,
	sat_act_college_ready_benchmark FLOAT,
    num_grade_12_meeting_benchmarks INT,
    number_grade_12_with_22_higher_act INT,
    number_grade_12_with_3_higher_ap_4_higher_ib INT,
    number_grade_12_taking_plan INT,
    number_grade_12_taking_psat INT,
    psat_plan_participation FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_ap_sat_act PRIMARY KEY (school_id, school_year)
);

CREATE TABLE public_school_grad_rates_district(
	district_aun INT,
    school_year INT,
	total_graduates INT,
    total_college_bound INT,
    total_college_bound_percentage FLOAT,
    two_four_year_college_university INT,
    two_four_year_college_university_percentage FLOAT,
    total_postsecondary_bound INT,
    total_postsecondary_bound_percentage FLOAT,
    non_degree_getting_postsecondary_school INT,
    non_degree_getting_postsecondary_school_percentage FLOAT,
    specialized_associate_degree_getting_institution INT,
    specialized_associate_degree_getting_institution_percentage FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_public_school_grad_rates_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE public_school_grad_rates_school(
	school_id INT,
    school_year INT,
	total_graduates INT,
    total_college_bound INT,
    total_college_bound_percentage FLOAT,
    two_four_year_college_university INT,
    two_four_year_college_university_percentage FLOAT,
    total_postsecondary_bound INT,
    total_postsecondary_bound_percentage FLOAT,
    non_degree_getting_postsecondary_school INT,
    non_degree_getting_postsecondary_school_percentage FLOAT,
    specialized_associate_degree_getting_institution INT,
    specialized_associate_degree_getting_institution_percentage FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_public_school_grad_rates_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE public_school_dropouts_school(
	school_id INT,
    school_year INT,
	oct_1_enrollment_grades_7_12 INT,
    male_dropouts INT,
    female_dropouts INT,
    dropouts INT,
    dropout_rate FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_public_school_dropouts_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE public_school_dropouts_district(
	district_aun INT,
    school_year INT,
	oct_1_enrollment_grades_7_12 INT,
    male_dropouts INT,
    female_dropouts INT,
    dropouts INT,
    dropout_rate FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_public_school_dropouts_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE keystone_grade_school(
	school_id INT,
    school_year INT,
	keystone_subject VARCHAR(25),
    student_group VARCHAR(75),
    grade INT,
    number_scored INT,
    percent_advanced FLOAT,
    percent_proficient FLOAT,
    percent_basic FLOAT,
    percent_below_basic FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_keystone_grade_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE grad_rate_by_race_school(
	school_id INT,
    school_year INT,
	x_year_cohort INT,
    aian_grad_rate FLOAT,
    native_hawaiin_pacific_islander_grad_rate FLOAT,
    asian_grad_rate FLOAT,
    black_grad_rate FLOAT,
    hispanic_grad_rate FLOAT,
    white_grad_rate FLOAT,
    multi_racial_grad_rate FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_grad_rate_by_race_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE grad_rate_by_category_school(
	school_id INT,
    school_year INT,
	x_year_cohort INT,
	cohort_grad_rate FLOAT,
    male_grad_rate FLOAT,
    female_grad_rate FLOAT,
    special_ed_grad_rate FLOAT,
    el_grad_rate FLOAT,
    econ_disadvantaged_grad_rate FLOAT,
    migrant_grad_rate FLOAT,
    foster_grad_rate FLOAT,
    homeless_grad_rate FLOAT,
    military_grad_rate FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_grad_rate_by_category_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE total_grads_school(
	school_id INT,
    school_year INT,
	x_year_cohort INT,
	grads INT,
    cohort INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_total_grads_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE grad_rate_by_race_district(
	district_aun INT,
    school_year INT,
	x_year_cohort INT,
    aian_grad_rate FLOAT,
    native_hawaiin_pacific_islander_grad_rate FLOAT,
    asian_grad_rate FLOAT,
    black_grad_rate FLOAT,
    hispanic_grad_rate FLOAT,
    white_grad_rate FLOAT,
    multi_racial_grad_rate FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_grad_rate_by_race_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE grad_rate_by_category_district(
	district_aun INT,
    school_year INT,
	x_year_cohort INT,
	cohort_grad_rate FLOAT,
    male_grad_rate FLOAT,
    female_grad_rate FLOAT,
    special_ed_grad_rate FLOAT,
    el_grad_rate FLOAT,
    econ_disadvantaged_grad_rate FLOAT,
    migrant_grad_rate FLOAT,
    foster_grad_rate FLOAT,
    homeless_grad_rate FLOAT,
    military_grad_rate FLOAT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_grad_rate_by_category_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE total_grads_district(
	district_aun INT,
    school_year INT,
	x_year_cohort INT,
	grads INT,
    cohort INT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_total_grads_district PRIMARY KEY (district_aun, school_year)
);

CREATE TABLE private_non_public_elem_enrollment_private_paid(
	school_id INT,
    school_year INT,
	k4 INT,
    k5 INT,
    grade_1 INT,
    grade_2 INT,
    grade_3 INT,
    grade_4 INT,
    grade_5 INT,
    grade_6 INT,
    grade_7E INT,
    grade_8E INT,
    total_elementary_ungraded INT,
    non_resident INT,
    resident INT,
    total_elementary_enrollment INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_elem_enrollment_private_paid PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_elem_enrollment_fully_public_paid(
	school_id INT,
    school_year INT,
	k4 INT,
    k5 INT,
    grade_1 INT,
    grade_2 INT,
    grade_3 INT,
    grade_4 INT,
    grade_5 INT,
    grade_6 INT,
    grade_7E INT,
    grade_8E INT,
    total_elementary_ungraded INT,
    non_resident INT,
    resident INT,
    total_elementary_enrollment INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_elem_enrollment_fully_public_paid PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_secondary_enrollment_private_paid(
	school_id INT,
    school_year INT,
	grade_9 INT,
    grade_10 INT,
    grade_11 INT,
    grade_12 INT,
    secondary_ungraded INT,
    non_resident INT,
    resident INT,
    total_secondary_enrollment INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_secondary_enrollment_private_paid PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_secondary_enrollment_fully_public_paid(
	school_id INT,
    school_year INT,
	grade_9 INT,
    grade_10 INT,
    grade_11 INT,
    grade_12 INT,
    secondary_ungraded INT,
    non_resident INT,
    resident INT,
    total_secondary_enrollment INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_secondary_enrollment_fully_public_paid PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_other_enrollment_private_paid(
	school_id INT,
    school_year INT,
	nursery INT,
    special_ed_preschool_k5 INT,
    special_ed_preschool_nursery_age_3_4_5 INT,
    non_resident INT,
    resident INT,
    total_other_enrollment INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_other_enrollment_private_paid PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_other_enrollment_public_paid(
	school_id INT,
    school_year INT,
	nursery INT,
    special_ed_preschool_k5 INT,
    special_ed_preschool_nursery_age_3_4_5 INT,
    non_resident INT,
    resident INT,
    total_other_enrollment INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_other_enrollment_public_paid PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_full_time_equivalent_teachers(
	school_id INT,
    school_year INT,
	nursery_fte FLOAT,
    elementary_fte FLOAT,
    secondary_fte FLOAT,
    special_education_fte FLOAT,
    total_fte FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_full_time_equivalent_teachers PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_low_income_enrollment(
	school_id INT,
    school_year INT,
	percent_nursery_low_income FLOAT,
    percent_k12_low_income FLOAT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_low_income_enrollment PRIMARY KEY (school_id, school_year)
);

CREATE TABLE private_non_public_total(
	school_id INT,
    school_year INT,
	grand_total INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_private_non_public_total PRIMARY KEY (school_id, school_year)
);

CREATE TABLE public_school_enrollment_school(
	school_id INT,
    school_year INT,
    pka INT,
    pkp INT,
    pkf INT,
    k4a INT,
    k4p INT,
    k4f INT,
    k5a INT,
    k5p INT,
    k5f INT,
    grade_1 INT,
    grade_2 INT,
    grade_3 INT,
    grade_4 INT,
    grade_5 INT,
    grade_6 INT,
    grade_7 INT,
    grade_8 INT,
    grade_9 INT,
    grade_10 INT,
    grade_11 INT,
    grade_12 INT,
    total INT,
    FOREIGN KEY (school_id) REFERENCES school(school_id),
    CONSTRAINT pk_public_school_enrollment_school PRIMARY KEY (school_id, school_year)
);

CREATE TABLE public_school_enrollment_district(
	district_aun INT,
    school_year INT,
    pka INT,
    pkp INT,
    pkf INT,
    k4a INT,
    k4p INT,
    k4f INT,
    k5a INT,
    k5p INT,
    k5f INT,
    grade_1 INT,
    grade_2 INT,
    grade_3 INT,
    grade_4 INT,
    grade_5 INT,
    grade_6 INT,
    grade_7 INT,
    grade_8 INT,
    grade_9 INT,
    grade_10 INT,
    grade_11 INT,
    grade_12 INT,
    total INT,
    FOREIGN KEY (district_aun) REFERENCES district(district_aun),
    CONSTRAINT pk_public_school_enrollment_district PRIMARY KEY (district_aun, school_year)
);