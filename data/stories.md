## student path
* greet
   - utter_ask_type
* current_student
   - info_form
    - form{"name":"info_form"}
    - slot{"requested_slot":"name"}
* name_entry{"name":"Meet"}
    - slot{"name":"Meet"}
    - slot{"name":"Meet"}
    - info_form
    - slot{"name":"Meet"}
    - slot{"requested_slot":"number"}
* number_entry{"number":"8928304380"}
    - slot{"number":"8928304380"}
    - slot{"number":"8928304380"}
    - info_form
    - slot{"number":"8928304380"}
    - slot{"requested_slot":"city"}
* ask_branch{"branch":"IT"}
    - slot{"branch":"IT"}
    - utter_submit
* student_affirm
    - utter_student_affirm
* time_table
    - utter_time_table
* results
    - utter_results
* intake
    - action_intake_api    
* gym
   - utter_gym
* gym_girls
   - utter_gym_girls
* events
   - utter_events
* itprof
   - action_itprof_api
* fees1
   - action_fees1_api
* fees2
   - action_fees2_api
* fees3
   - action_fees3_api
* fees4
   - action_fees4_api
* register
  -  action_register_api
* contact
   - action_contact_api
* thanks
  - utter_thanks 
* goodbye
  - utter_goodbye
* bot_challenge
  - utter_iamabot
* address
  - utter_address





## Happy Parent 
* greet
   - utter_ask_type
* parent
    - utter_parent_affirm
* courses
    - utter_courses
* office_number
    - utter_office_number
* principal
    - utter_principal
* affiliation
    - utter_affiliation
* working_hours
    - utter_working_hours
* thanks
    - utter_thanks

<!-- ## parent path
* greet
    - utter_ask_type
* parent
    - info_form
    - form{"name":"info_form"}
    - slot{"requested_slot":"name"}
* name_entry{"name":"Meet"}
    - slot{"name":"Meet"}
    - slot{"name":"Meet"}
    - info_form
    - slot{"name":"Meet"}
    - slot{"requested_slot":"number"}
* number_entry{"number":"8928304380"}
    - slot{"number":"8928304380"}
    - slot{"number":"8928304380"}
    - info_form
    - slot{"number":"8928304380"}
    - slot{"requested_slot":"city"}
* ask_branch{"branch":"IT"}
    - slot{"branch":"IT"}
    - utter_parent_submit
* parent_affirm
    - utter_parent_affirm
* principal
    - utter_principal
* working_hours
	- utter_working_hours
* office_number
	- utter_office_number
* affiliation
	- utter_affiliation -->

## happy itprof

* itprof
  - action_itprof_api

##happy fees1
 
 * fees1
   - action_fees1_api

##happy fees2
 
 * fees2
   - action_fees2_api

##happy fees3
 
 * fees3
   - action_fees3_api

##happy fees4
 
 * fees4
   - action_fees4_api

## happy register
 
 * register
  - action_register_api

##  happy contact
  
  * contact
   - action_contact_api




