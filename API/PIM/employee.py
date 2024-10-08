import requests


class APIEmployee:
    @staticmethod
    def api_delete_employee_by_id(employee_id, session_cookie):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees"

        headers = {
            "Cookie": f"orangehrm={session_cookie}",
        }

        payload = {"ids": [employee_id]}
        response = requests.delete(url, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"Employee with ID {employee_id} successfully deleted.")
        else:
            raise AssertionError(f"Failed to delete employee. Status code: {response.status_code}, "
                                 f"Response: {response.text}")
