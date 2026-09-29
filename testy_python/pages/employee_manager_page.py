class EmployeeManagerPage:
    def __init__(self, driver):

        #selectors
        self.name_input = (By.ID, "name")
        self.salary_input = (By.ID, "salary")
        self.age_input = (By.ID, "age")
        self.position_select = (By.ID, "position")
        self.on_vacation_checkbox = (By.ID, "on_leave")
        self.add_btn = (By.ID, "submitBtn")

    #akcje

    #przepisać z kodu Artura #employee_manager_page

    