from dataclasses import dataclass, field
from typing import List
import sys

REQUIRED_PYTHON_VERSION = (3, 7)

if sys.version_info < REQUIRED_PYTHON_VERSION:
    print("Python version {} or higher is required.".format(".".join(map(str, REQUIRED_PYTHON_VERSION))))
    print("Shoot an email to chorlick@gmail.com for a copy of his resume or see it here")
    print("https://github.com/chorlick/resume/resume.txt")
    sys.exit(1)


@dataclass
class Experience:
    title: str
    company: str
    location: str
    dates: str
    responsibilities: List[str]

@dataclass
class Education:
    degree: str
    institution: str
    dates: str

@dataclass
class SkillSection:
    category: str
    skills: List[str]

@dataclass
class Certification:
    title: str
    description: str

@dataclass
class Resume:
    name: str
    title: str
    contact_info: dict
    summary: str
    experiences: List[Experience] = field(default_factory=list)
    education: List[Education] = field(default_factory=list)
    skills: List[SkillSection] = field(default_factory=list)
    certifications: List[Certification] = field(default_factory=list)
    additional_info: dict = field(default_factory=dict)

    def display(self):
        print(f"{self.name}")
        print(f"{self.title}")
        print(f"{self.contact_info.get('Location')}")
        print(f"Email: {self.contact_info.get('Email')} | Phone: {self.contact_info.get('Phone')} | GitHub: {self.contact_info.get('GitHub')}\n")
        
        print("Summary")
        print(self.summary + "\n")
        
        print("Professional Experience")
        for exp in self.experiences:
            print(f"{exp.title}")
            print(f"{exp.company} | {exp.location} | {exp.dates}")
            for resp in exp.responsibilities:
                print(f"- {resp}")
            print()
        
        print("Education")
        for edu in self.education:
            print(f"{edu.degree}")
            print(f"{edu.institution} | {edu.dates}")
            print()
        
        print("Skills")
        for skill_section in self.skills:
            print(f"{skill_section.category}: {', '.join(skill_section.skills)}")
        print()
        
        print("Certifications & Achievements")
        for cert in self.certifications:
            print(f"{cert.title}")
            print(f"{cert.description}\n")
        
        print("Additional Information")
        for key, value in self.additional_info.items():
            print(f"{key}: {value}")
        print()

if __name__ == "__main__":
    resume = Resume(
        name="CHRISTOPHER M. HORLICK",
        title="Senior Software Engineer",
        contact_info={
            "Email": "chorlick@gmail.com",
            "Phone": "256-479-9562",
            "GitHub": "github.com/chorlick",
            "Location": "Madison, AL, USA"
        },
        summary=(
            "Senior Software Engineer with over 15 years of experience specializing in C++ and Qt application development. "
            "Expertise in designing and deploying cross-platform applications, user interface design with QML, and developing robust software systems. "
            "Proven ability to lead projects from concept to deployment, collaborate with cross-functional teams, and deliver high-quality, production-ready code. "
            "Seeking to contribute my skills to Performance Drone Works (PDW) and support the advancement of sUAS functional systems."
        ),
        experiences=[
            Experience(
                title="C++ Senior Software Developer",
                company="Global Payments, Inc.",
                location="Remote (Atlanta, GA)",
                dates="Sep 2020 – Sep 2024",
                responsibilities=[
                    "Developed and maintained high-performance C++ applications for payment processing systems.",
                    "Led the transition from SVN to Git, enhancing version control efficiency.",
                    "Automated deployment tasks using Python and Bash scripting."
                ]
            ),
            Experience(
                title="C++ and Qt Software Developer",
                company="Geeks and Nerds",
                location="Huntsville, AL",
                dates="Jan 2014 – Jan 2016",
                responsibilities=[
                    "Developed Linux-based C++ and Qt applications for the Army Redstone Test Center (RTC).",
                    "Designed and implemented user interfaces using QML.",
                    "Managed code versioning with Git and issue tracking with Jira."
                ]
            ),
            Experience(
                title="Software Engineer",
                company="Independent Contractor",
                location="Various Locations",
                dates="Jan 2012 – Jan 2018",
                responsibilities=[
                    "Completed C++ development projects in both application and kernel space.",
                    "Developed cross-platform applications with Qt and conducted hardware layout and microcontroller development.",
                    "Worked independently while maintaining clear communication with stakeholders."
                ]
            ),
            Experience(
                title="Software Engineer",
                company="Pikewerks",
                location="Madison, AL",
                dates="Jan 2009 – Jan 2010",
                responsibilities=[
                    "Developed Linux kernel modules focusing on networking capabilities in C++.",
                    "Created rapid development tools using Python and PyQt.",
                    "Identified and addressed performance bottlenecks and security vulnerabilities."
                ]
            ),
        ],
        education=[
            Education(
                degree="Ph.D. in Computer Engineering (In Progress)",
                institution="The University of Alabama in Huntsville",
                dates="Sep 2022 – Present"
            ),
            Education(
                degree="Master of Software Engineering",
                institution="Regis University",
                dates="2017"
            ),
            Education(
                degree="Bachelor of Science in Computer Science",
                institution="Athens State University",
                dates="2014"
            )
        ],
        skills=[
            SkillSection(
                category="Programming Languages",
                skills=["C++ (Expert)", "Python", "Java", "JavaScript", "Bash", "TypeScript"]
            ),
            SkillSection(
                category="Frameworks & Tools",
                skills=["Qt", "QML", "CMake", "QMake", "Git", "Jira", "REST APIs", "JSON"]
            ),
            SkillSection(
                category="Development Practices",
                skills=["Cross-platform development", "Embedded Linux", "Android development", "Code reviews", "Unit testing"]
            ),
            SkillSection(
                category="Other Technologies",
                skills=["Build tools", "Compiler configuration", "Third-party libraries and APIs", "Remote data integration"]
            )
        ],
        certifications=[
            Certification(
                title="S3I Challenge Coin Recipient",
                description="Awarded by the U.S. Military for outstanding team contributions."
            ),
            Certification(
                title="SAIC Fellow",
                description="Mentored incoming students to develop industry-standard skills."
            )
        ],
        additional_info={
            "Security Clearance": "Eligible under ITAR requirements; U.S. Citizen",
            "Passions": "Software Craftsmanship, Artificial Intelligence, Cybersecurity, Drone Swarms"
        }
    )

    resume.display()