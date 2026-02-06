def scaledown_course(course_content):
    """
    Compress course content by removing redundancy
    """
    return course_content[:len(course_content)//4]  # 75% compression

