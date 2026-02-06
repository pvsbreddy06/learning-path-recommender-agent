def track_progress(progress_data):
    completed = progress_data.get("completed_modules", 0)
    total = progress_data.get("total_modules", 1)

    progress_percent = (completed / total) * 100

    return {
        "progress": progress_percent,
        "status": "On Track" if progress_percent > 50 else "Needs Attention"
    }

