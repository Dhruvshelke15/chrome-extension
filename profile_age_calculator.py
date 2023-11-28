from datetime import datetime

class ProfileAgeCalculator:
    @staticmethod
    def calculate_age(profile):

        if 'education' in profile:
            education_year = profile['education']
            return datetime.now().year - education_year + 18


        if 'work_experience' in profile:
            first_job_year = profile['work_experience'][0]['start_year']
            return datetime.now().year - first_job_year + 22

 
        return None
