-- searched CASE (flexible)
CASE WHEN status = 'A' THEN 'Active' END

-- simple CASE (shorthand)
CASE status
  WHEN 'A' THEN 'Active'
  WHEN 'X' THEN 'Closed'
END
