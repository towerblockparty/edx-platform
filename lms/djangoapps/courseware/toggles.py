"""
Toggles for courseware in-course experience.
"""

from django.conf import settings
from lms.djangoapps.experiments.flags import ExperimentWaffleFlag
from openedx.core.djangoapps.waffle_utils import CourseWaffleFlag, WaffleFlagNamespace

# Namespace for courseware waffle flags.
WAFFLE_FLAG_NAMESPACE = WaffleFlagNamespace(name='courseware')

# Waffle flag to redirect to another learner profile experience.
# .. toggle_name: courseware.courseware_mfe
# .. toggle_implementation: ExperimentWaffleFlag
# .. toggle_default: False
# .. toggle_description: Supports staged rollout to students for a new micro-frontend-based implementation of the courseware page.
# .. toggle_category: micro-frontend
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: 2020-01-29
# .. toggle_expiration_date: 2020-12-31
# .. toggle_warnings: Also set settings.LEARNING_MICROFRONTEND_URL and ENABLE_COURSEWARE_MICROFRONTEND.
# .. toggle_tickets: TNL-7000
# .. toggle_status: supported
REDIRECT_TO_COURSEWARE_MICROFRONTEND = ExperimentWaffleFlag(
    WAFFLE_FLAG_NAMESPACE, 'courseware_mfe', use_course_aware_bucketing=False
)

# Waffle flag to display a link for the new learner experience to course teams without redirecting students.
#
# .. toggle_name: courseware.microfrontend_course_team_preview
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Supports staged rollout to course teams of a new micro-frontend-based implementation of the courseware page.
# .. toggle_category: micro-frontend
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: 2020-03-09
# .. toggle_expiration_date: 2020-12-31
# .. toggle_warnings: Also set settings.LEARNING_MICROFRONTEND_URL and ENABLE_COURSEWARE_MICROFRONTEND.
# .. toggle_tickets: TNL-6982
# .. toggle_status: supported
COURSEWARE_MICROFRONTEND_COURSE_TEAM_PREVIEW = CourseWaffleFlag(WAFFLE_FLAG_NAMESPACE, 'microfrontend_course_team_preview')


# Waffle flag to enable the course completion page in the learning MFE.
#
# .. toggle_name: courseware.courseware_mfe_course_completion
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Supports staged rollout of the new micro-frontend-based implementation of the course completion page.
# .. toggle_category: micro-frontend
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: 2020-09-09
# .. toggle_expiration_date: 2020-12-31
# .. toggle_warnings: Also set settings.LEARNING_MICROFRONTEND_URL and ENABLE_COURSEWARE_MICROFRONTEND.
# .. toggle_tickets: AA-196
# .. toggle_status: supported
COURSEWARE_MICROFRONTEND_COURSE_COMPLETION = CourseWaffleFlag(
    WAFFLE_FLAG_NAMESPACE, 'courseware_mfe_course_completion'
)


def course_completion_is_active(course_key):
    return (
        REDIRECT_TO_COURSEWARE_MICROFRONTEND.is_enabled(course_key) and
        COURSEWARE_MICROFRONTEND_COURSE_COMPLETION.is_enabled(course_key)
    )
