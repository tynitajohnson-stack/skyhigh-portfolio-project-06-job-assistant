Ticket 0: Target Role Research

Project Overview

The SoleCloud Job Application Assistant is a local-first application designed to help job seekers discover relevant opportunities, tailor application materials, and track their job search progress.

The application will not automatically submit job applications. Users must review their materials and submit applications themselves.

1. Target Job Roles

The application will initially focus on the following roles:

- Cloud Engineer
- Junior Cloud Engineer
- AWS Cloud Support Engineer
- Cybersecurity Analyst
- Cloud Security Analyst
- Governance, Risk, and Compliance (GRC) Analyst

2. Common Technical Skills

**Cloud Computing**
- Amazon Web Services (AWS)
- EC2, S3, IAM, and VPC
- CloudWatch monitoring
- Cloud infrastructure troubleshooting

**Infrastructure and Automation**
- Terraform
- Infrastructure as Code (IaC)
- Linux administration
- Python scripting
- Git and GitHub

**Cybersecurity**
- Identity and Access Management
- Security monitoring
- Risk assessments
- Security policies and compliance
- Vulnerability management

3. Certifications and Qualifications

Relevant qualifications include:

- CompTIA Security+
- AWS Certified Cloud Practitioner
- AWS Certified Solutions Architect – Associate
- Bachelor's degree in Information Technology or related fields
- Experience with cloud platforms, security tools, or technical troubleshooting

These are examples of potentially relevant qualifications, not requirements for every role.

4. Job Matching Keywords

The application should identify keywords such as:

- AWS
- Cloud Infrastructure
- Terraform
- Python
- Linux
- IAM
- EC2
- S3
- CloudWatch
- Cybersecurity
- Risk Management
- Compliance
- Incident Response
- Infrastructure as Code

5. Application Tailoring Strategy

The assistant will compare job descriptions with a user's documented skills and experience.

It should:

1. Identify relevant skills and keywords from job descriptions.
2. Compare those requirements against the user's profile.
3. Highlight matching qualifications.
4. Suggest truthful resume improvements.
5. Identify skills or experience gaps.
6. Prepare materials for human review.

The application must never invent certifications, work experience, or qualifications.

6. Approved Job Sources

The application will retrieve job opportunities using permitted sources, including:

- Greenhouse public job APIs
- Lever public job APIs
- Public company career feeds
- RSS feeds where available

The application will not scrape LinkedIn, Indeed, or restricted applicant tracking systems.

7. Project Guardrails

- Local-first development with no cloud deployment.
- No automatic application submission.
- No prohibited scraping.
- No API keys or credentials committed to GitHub.
- Reusable components separated from role-specific configuration.
- Human review required before any application is submitted.

8. Research Summary

This research establishes an initial set of target roles, technical skills, certifications, and job-matching keywords for the SoleCloud Job Application Assistant.

These findings will guide the development of the job aggregation and application tailoring features. Before implementing role-specific matching, the requirements should be validated against actual job postings from approved sources.
