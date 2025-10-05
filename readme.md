Multi-Agent LangGraph Architecture for Career-Compass++
1. Agents & Roles

Job Market Agent

Input: Job title/field from user

Action: Scrape job portals (e.g., LinkedIn, Indeed API, Kaggle datasets)

Output: Current demand, trending skills, required tools/tech stack

Resume Analysis Agent

Input: User’s resume (PDF/DOCX)

Action: Extracts text → NLP parsing → Identifies skills, experience, keywords

Output: List of strengths, weak points, ATS (Applicant Tracking System) score

Skill Gap Agent

Input: Job Market Agent output + Resume Analysis Agent output

Action: Compare market demands vs user resume

Output: Missing skills, outdated skills, suggested improvements

Mentor Agent

Input: Skill Gap results

Action: Suggests learning resources (Coursera, Udemy, GitHub repos), projects to build, and career path suggestions

Output: Action plan → “Learn X, build Y project, apply to Z role”