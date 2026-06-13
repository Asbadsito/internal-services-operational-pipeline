CREATE OR REPLACE VIEW v_clean_employees AS
SELECT employee_id, first_name, last_name, department, region, hire_date
FROM dim_employees;

CREATE OR REPLACE VIEW v_compliance_ticket_metrics AS
SELECT 
    ticket_id, employee_id, issue_type, severity, status, created_date, resolved_date,
    COALESCE(resolved_date, CURRENT_DATE) as effective_closed_date,
    CASE 
        WHEN resolved_date IS NOT NULL THEN (resolved_date - created_date)
        ELSE (CURRENT_DATE - created_date)
    END as ticket_age_days,
    risk_score,
    CASE 
        WHEN risk_score >= 80 OR severity = 'Critical' THEN 'Immediate Escalation Required'
        ELSE 'Standard Operational Tracking'
    END as governance_status
FROM fact_compliance_tickets;
