import requests


class APIEmployee:
    api_employee_url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees"

    @staticmethod
    def get_headers(session_cookie):
        return {
            "Cookie": f"orangehrm={session_cookie}"
        }

    @staticmethod
    def api_delete_employee_by_id(employee_id, session_cookie):
        headers = APIEmployee.get_headers(session_cookie)
        payload = {"ids": [employee_id]}
        response = requests.delete(APIEmployee.api_employee_url, json=payload, headers=headers)

        if response.status_code != 200:
            raise AssertionError(f"Failed to delete employee. Status code: {response.status_code}, "
                                 f"Response: {response.text}")

    @staticmethod
    def api_create_employee(session_cookie, emp_picture=None):
        headers = APIEmployee.get_headers(session_cookie)
        payload = {
            "firstName": "First",
            "middleName": "Middle",
            "lastName": "Last",
            "empPicture": emp_picture,
            "employeeId": ""
        }
        response = requests.post(APIEmployee.api_employee_url, json=payload, headers=headers)

        if response.status_code != 200:
            raise AssertionError(f"Failed to create employee. Status code: {response.status_code}, "
                                 f"Response: {response.text}")
