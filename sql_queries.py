import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

dim_teachers_table_drop = "DROP TABLE IF EXISTS dim_teachers"
dim_donors_table_drop = "DROP TABLE IF EXISTS dim_donors"
dim_schools_table_drop = "DROP TABLE IF EXISTS dim_schools"
fact_donations_table_drop = "DROP TABLE IF EXISTS fact_donations"


# CREATE TABLES

dim_teachers_table_create = ("""CREATE TABLE IF NOT EXISTS dim_teachers (
                                teacher_id  VARCHAR(255)  PRIMARY KEY,
                                teacher_prefix  VARCHAR(20),
                                teacher_first_project_posted_date DATE
                                );
                            """)

dim_donors_table_create = ("""CREATE TABLE IF NOT EXISTS dim_donors (
                                donor_id  VARCHAR(255)  PRIMARY KEY,
                                donor_city  VARCHAR(50),
                                donor_state  VARCHAR(20),
                                donor_is_teacher  VARCHAR(10)
                                );
                            """)

dim_schools_table_create = ("""CREATE TABLE IF NOT EXISTS dim_schools (
                            school_id  VARCHAR(255)  PRIMARY KEY,
                            school_name  VARCHAR(255),
                            school_state  VARCHAR(50),
                            school_city  VARCHAR(100),
                            school_metro_type  VARCHAR(50),
                            school_percentage_free_lunch  INT,
                            free_lunch_level  VARCHAR(20)
                            );
                        """)

fact_donations_table_create = ("""CREATE TABLE IF NOT EXISTS fact_donations (
                        project_id  VARCHAR(255),
                        donation_id  VARCHAR(255)  PRIMARY KEY,
                        donor_id  VARCHAR(255),
                        donation_included_optional_donation VARCHAR(10),
                        donation_amount  NUMERIC,
                        donation_received_date  DATE,
                        year  INT,
                        school_id  VARCHAR(255),
                        teacher_id  VARCHAR(255),
                        project_type  VARCHAR(50),
                        project_grade_level_category  VARCHAR(20),
                        project_cost  NUMERIC,
                        project_posted_date  DATE,
                        project_expiration_date  DATE,
                        project_fully_funded_date  DATE
                        );
                    """)


# LOADING TABLES

dim_teachers_copy = ("""
                    copy dim_teachers from '{}'
                    credentials 'aws_iam_role={}'
                    region 'us-west-2'
                    compupdate off
                    format as csv
                    """).format(config.get('S3', 'TEACHERS_DATA'),
                                config.get('IAM_ROLE', 'ARN'))

dim_donors_copy = ("""
                        copy dim_donors from '{}'
                        credentials 'aws_iam_role={}'
                        region 'us-west-2'
                        compupdate off
                        format as csv
                        """).format(config.get('S3', 'DONORS_DATA'),
                                    config.get('IAM_ROLE', 'ARN'))

dim_schools_copy = ("""
                        copy dim_schools from '{}'
                        credentials 'aws_iam_role={}'
                        region 'us-west-2'
                        compupdate off
                        format as csv
                        """).format(config.get('S3', 'SCHOOLS_DATA'),
                                    config.get('IAM_ROLE', 'ARN'))


fact_donations_copy = ("""
                        copy fact_donations from '{}'
                        credentials 'aws_iam_role={}'
                        region 'us-west-2'
                        compupdate off
                        format as csv
                        """).format(config.get('S3', 'DONATIONS_DATA'),
                                    config.get('IAM_ROLE', 'ARN'))


# QUERY LISTS

drop_table_queries = [dim_teachers_table_drop, dim_donors_table_drop, dim_schools_table_drop, fact_donations_table_drop]
create_table_queries = [dim_teachers_table_create, dim_donors_table_create, dim_schools_table_create, fact_donations_table_create]
copy_table_queries = [dim_teachers_copy, dim_donors_copy, dim_schools_copy, fact_donations_copy]
