# Data Dictionary

### Dimension Tables:

    - dim_teachers
    - dim_donors
    - dim_schools

### Fact Table:

    - fact_donations

### Database Model

![title](img/ERD.png)


## Description

### dim_teachers
* __teacher_id__: Unique identifier of a teacher.
* __teacher_prefix__: Prefix of the teacher ("Mrs.", "Ms.", "Mr.", "Teacher" etc.)
* __teacher_first_project_posted_date__: Date on which the teacher’s first project was posted.


### dim_donors

* __donor_id__: Unique identifier of a donor.
* __donor_city__: The donor’s city. 
* __donor_state__: The donor’s state.
* __donor_is_teacher__: Whether or not the donor is a teacher.


### dim_schools

- __school_id__: Unique identifier of a school.
- __school_name__: Name of the school.
- __school_state__: The state of the school that the teacher was teaching at at the time the project was posted.
- __school_city__: The city of the school that the teacher was teaching at at the time the project was posted.
- __school_metro_type__: Metro type of school area ("urban", "suburban", "rural", "town" etc.) .
- __school_percentage_free_lunch__: Integer describing percentage of students qualifying for free or reduced lunch, 
									obtained from NCES data. For schools without NCES data, a district average is used.
- __free_lunch_level__: "high" if percentage between 60 to 100, "medium” if percentage between 30 to 60, 
						"low" if percentage between 0 to 30, "NA" if pecentage is missing.

### fact_donations

* __donation_id__: Unique ID of a donation.
* __project_id__: Unique ID of a project.
* __donor_id__: Unique ID of a donor.
* __school_id__: Unique identifier of a school.
* __teacher_id__: Unique identifier of a teacher.
* __donation_amount__: Total amount donated for a project.
* __donation_received_date__: Date on which the donation was recieved.
* __year__: Year on which the donation was received.
* __donation_included_optional_donation__: Yes/No to give 15% of donation amount to Donoschoose.
* __project_type__: Type of project ("Teacher-Led", “Student-led", "Professional Development").
* __project_grade_level_category__: Grade level category of project ("Grades PreK-2", "Grades 9-12" etc.).
* __project_cost__: Total cost of project.
* __project_posted_date__: Date on which the project is posted.
* __project_expiration_date__: Date on which the project is expired.
* __project_fully_funded_date__: Date on which the project is fully funded.