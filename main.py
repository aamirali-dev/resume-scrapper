from extractors.enhancv import EnhanCVExtractor
from extractors.resumeexample import ResumeExampleExtractor
from extractors.resumeio import ResumeIOExtractor
from extractors.resumebuilder import ResumeBuilderExtractor
from extractors.resumegenius import ResumeGeniusExtractor
from extractors.zety import ZetyExtractor

if __name__ == "__main__":
    with_resumes = [ResumeBuilderExtractor, ResumeGeniusExtractor, ZetyExtractor]
    only_categories = [EnhanCVExtractor, ResumeExampleExtractor, ResumeIOExtractor]

    for extractor in only_categories:
        rexec = extractor()
        print(extractor.__class__.__name__)
        print(rexec.extract_resume_categories())

    for extractor in with_resumes:
        rexec = extractor()
        print(rexec.extract_resume_categories())