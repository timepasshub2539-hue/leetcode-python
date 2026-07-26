SELECT e.employee_name, m.manager_name FROM staff e CROSS JOIN staff m WHERE e.supervisor_id = m.staff_id;
