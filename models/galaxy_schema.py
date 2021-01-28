"""Schema for Ansible Galaxy API."""
from typing import Any, Dict

import pendulum

# Schemas
SCHEMAS: Dict[str, Dict[str, Any]] = {
    'community_surveys': {
        'active': None,
        'content_id': int,
        'created': pendulum.DateTime,
        'docs': (int, None),
        'does_what_it_says': (int, None),
        'ease_of_use': (int, None),
        'id': int,
        'modified': pendulum.DateTime,
        'related': {},
        'repository': int,
        'summary_fields': {
            'content': {
                'community_score': (float, None),
                'name': str,
                'type': 'repository'
            }
        },
        'url': str,
        'used_in_production': (int, None),
        'user': int,
        'works_as_is': (int, None),
    },
    'content': {
        'compatibility_score': None,
        'content_score': (float, None),
        'content_type': str,
        'created': pendulum.DateTime,
        'description': str,
        'download_count': int,
        'id': int,
        'imported': (pendulum.DateTime, None),
        'metadata_score': (float, None),
        'modified': pendulum.DateTime,
        'name': str,
        'original_name': str,
        'quality_score': (float, None),
        'related': {
            'content_type': str,
            'dependencies': str,
            'imports': str,
            'namespace': str,
            'provider': '/api/v1/providers/active/1/',
            'provider_namespace': str,
            'repository': str,
        },
        'role_type': ('ANS', 'CON', 'APP', None),
        'summary_fields': {
            'content_type': {
                'description': str,
                'id': int,
                'name': str,
            },
            'dependencies': [str],
            'namespace': {
                'id': int,
                'is_vendor': False,
                'name': str,
            },
            'repository': {
                'clone_url': str,
                'deprecated': bool,
                'description': str,
                'id': int,
                'name': str,
                'original_name': str,
            },
            'task_messages': [{
                'content_id': int,
                'id': int,
                'is_linter_rule_violation': bool,
                'linter_rule_id': str,
                'linter_type': str,
                'message_text': str,
                'message_type': 'WARNING',
                'rule_desc': str,
                'rule_severity': (int, None),
                'score_type': ('content', 'metadata', None)
            }],
        },
        'url': str,
    },
    'namespaces': {
        'active': bool,
        'avatar_url': (str, None),
        'company': (str, None),
        'created': pendulum.DateTime,
        'description': (str, None),
        'email': (str, None),
        'html_url': (str, None),
        'id': int,
        'is_vendor': False,
        'location': (str, None),
        'modified': pendulum.DateTime,
        'name': str,
        'related': {
            'content': str,
            'owners': str,
            'provider_namespaces': str,
        },
        'summary_fields': {
            'content_counts': {
                'role': int,
                'apb': int,
                'module': int,
                'module_utils': int,
                'filter': int,
                'strategy': int,
                'action': int,
                'lookup': int,
                'callback': int,
                'inventory': int,
            },
            'owners': [{
                'avatar_url': str,
                'id': int,
                'username': str,
            }],
            'provider_namespaces': [{
                'avatar_url': (str, None),
                'compay': (str, None),
                'description': str,
                'display_name': (str, None),
                'email': (str, None),
                'html_url': (str, None),
                'id': int,
                'location': (str, None),
                'name': str,
                'provider': 1,
                'provider_name': 'github',
            }],
        },
        'url': str,
    },
    'platforms': {
        'active': True,
        'created': pendulum.DateTime,
        'id': int,
        'modified': pendulum.DateTime,
        'name': str,
        'related': {},
        'release': str,
        'summary_fields': {},
        'url': str,
    },
    'provider_namespaces': {
        'active': True,
        'avatar_url': (str, None),
        'company': (str, None),
        'created': pendulum.DateTime,
        'description': str,
        'display_name': (str, None),
        'email': (str, None),
        'followers': (int, None),
        'html_url': (str, None),
        'id': int,
        'location': (str, None),
        'modified': pendulum.DateTime,
        'name': str,
        'related': {
            'namespace': str,
            'provider': '/api/v1/providers/active/1/',
            'repositories': str,
        },
        'summary_fields': {
            'namespace': {
                  'id': int,
                  'is_vendor': False,
                  'name': str,
            },
            'provider': {
              'id': 1,
              'name': "GitHub"
            },
        },
        'url': str,
    },
    'repositories': {
        'active': None,
        'clone_url': str,
        'commit': str,
        'commit_created': (pendulum.DateTime, None),
        'commit_message': str,
        'commit_url': str,
        'community_score': (float, None),
        'community_survey_count': int,
        'created': pendulum.DateTime,
        'deprecated': bool,
        'description': str,
        'download_count': int,
        'download_url': str,
        'external_url': str,
        'forks_count': int,
        'format': (str, None),
        'id': int,
        'import_branch': (str, None),
        'is_enabled': bool,
        'issue_tracker_url': (str, None),
        'modified': pendulum.DateTime,
        'name': str,
        'open_issues_count': int,
        'original_name': str,
        'quality_score': (float, None),
        'quality_score_date': (pendulum.DateTime, None),
        'readme': (str, None),
        'readme_html': (str, None),
        'related': {
            'content': str,
            'imports': str,
            'namespace': str,
            'provider': str,
            'provider_namespace': str,
            'versions': str
        },
        'stargazers_count': int,
        'summary_fields': {
            'content_counts': {
                'role': int,
                'apb': int,
                'strategy': int,
                'module_utils': int,
                'filter': int,
                'lookup': int,
                'action': int,
                'module': int,
                'callback': int,
                'inventory': int,
            },
            'content_objects': [{
                'content_type': str,
                'description': str,
                'id': int,
                'name': str,
                'quality_score': (float, None),
            }],
            'latest_import': {
                  'created': pendulum.DateTime,
                  'finished': (pendulum.DateTime, None),
                  'id': int,
                  'modified': pendulum.DateTime,
                  'started': (pendulum.DateTime, None),
                  'state': ('SUCCESS', 'FAILED'),
            },
            'namespace': {
                  'description': str,
                  'id': int,
                  'is_vendor': False,
                  'name': str
            },
            'owners': [{
                'avatar_url': str,
                'id': int,
                'username': str
            }],
            'provider': {
                  'id': 1,
                  'name': 'GitHub'
            },
            'provider_namespace': {
                  'id': int,
                  'name': str,
            },
            'versions': [{
                'download_url': str,
                'version': str,
            }]
        },
        'travis_build_url': str,
        'travis_status_url': str,
        'url': str,
        'watchers_count': int
    },
    'role_search': {
        'active': True,
        'commit': str,
        'commit_message': str,
        'commit_url': str,
        'company': (str, None),
        'created': pendulum.DateTime,
        'description': str,
        'download_count': int,
        'download_rank': float,
        'forks_count': int,
        'github_branch': str,
        'github_repo': str,
        'github_user': str,
        'id': int,
        'imported': (pendulum.DateTime, None),
        'is_valid': bool,
        'issue_tracker_url': (str, None),
        'license': str,
        'min_ansible_version': (str, None),
        'modified': pendulum.DateTime,
        'name': str,
        'open_issues_count': int,
        'related': {
            'content_type': '/api/v1/content_types/11/',
            'dependencies': str,
            'imports': str,
        },
        'relevance': float,
        'role_type': ('ANS', 'CON', 'APP'),
        'search_rank': 0.0,
        'stargazers_count': int,
        'summary_fields': {
            'content_type': {
              'description': 'Role',
              'id': 11,
              'name': 'role'
            },
            'dependencies': [str],
            'namespace': {
              'avatar_url': (str, None),
              'company': (str, None),
              'email': (str, None),
              'html_url': (str, None),
              'id': int,
              'is_vendor': False,
              'location': (str, None),
              'name': str
            },
            'platforms': [{
                'name': str,
                'release': str,
            }],
            'provider_namespace': {
                  'id': int,
                  'name': str
            },
            'repository': {
                  'community_score': (float, None),
                  'community_survey_count': int,
                  'deprecated': bool,
                  'forks_count': int,
                  'format': ('role', 'multi'),
                  'id': int,
                  'name': str,
                  'open_issues_count': int,
                  'original_name': str,
                  'quality_score': (float, None),
                  'stargazers_count': int,
                  'travis_build_url': str,
                  'travis_status_url': str,
                  'watchers_count': int
            },
            'tags': [str],
            'versions': [{
                'id': int,
                'name': str,
                'release_date': (pendulum.DateTime, None),
            }],
            'videos': []
        },
        'travis_status_url': str,
        'url': str,
        'username': str,
    },
    'roles': {
        'active': True,
        'commit': str,
        'commit_message': str,
        'commit_url': str,
        'company': (str, None),
        'created': pendulum.DateTime,
        'description': str,
        'download_count': int,
        'forks_count': int,
        'github_branch': str,
        'github_repo': str,
        'github_user': str,
        'id': int,
        'imported': (pendulum.DateTime, None),
        'is_valid': bool,
        'issue_tracker_url': (str, None),
        'license': str,
        'min_ansible_version': (str, None),
        'modified': pendulum.DateTime,
        'name': str,
        'namespace': int,
        'open_issues_count': int,
        'readme': (str, None),
        'readme_html': (str, None),
        'related': {
            'content_type': str,
            'dependencies': str,
            'imports': str,
        },
        'relevance': float,
        'role_type': ('ANS', 'CON', 'APP', None),
        'stargazers_count': int,
        'summary_fields': {
            'content_type': {
              'description': str,
              'id': int,
              'name': str,
            },
            'dependencies': [(str, {
                'id': int,
                'name': str,
            })],
            'namespace': {
              'avatar_url': (str, None),
              'company': (str, None),
              'email': (str, None),
              'html_url': (str, None),
              'id': int,
              'is_vendor': False,
              'location': (str, None),
              'name': str
            },
            'platforms': [{
                'name': str,
                'release': str,
            }],
            'provider_namespace': {
                  'id': int,
                  'name': str
            },
            'repository': {
                  'community_score': (float, None),
                  'community_survey_count': int,
                  'deprecated': bool,
                  'forks_count': int,
                  'format': str,
                  'id': int,
                  'name': str,
                  'open_issues_count': int,
                  'original_name': str,
                  'quality_score': (float, None),
                  'stargazers_count': int,
                  'travis_build_url': str,
                  'travis_status_url': str,
                  'watchers_count': int
            },
            'tags': [str],
            'versions': [{
                'id': int,
                'name': str,
                'release_date': (pendulum.DateTime, None),
            }],
            'videos': []
        },
        'travis_status_url': str,
        'url': str,
        'username': str,
    },
    'tags': {
        'active': True,
        'created': pendulum.DateTime,
        'id': int,
        'modified': pendulum.DateTime,
        'name': str,
        'related': {},
        'summary_fields': {},
        'url': str,
    },
}
_ = {
    'users': {
        'active': True,
        'avatar_url': str,
        'created': pendulum.DateTime,
        'date_joined': pendulum.DateTime,
        'full_name': str,
        'id': int,
        'modified': (pendulum.DateTime, None),
        'related': {
            'email': str,
            'repositories': str,
            'starred': str,
            'subscriptions': str,
        },
        'staff': bool,
        'summary_fields': {
            'starred': [{
                'github_repo': str,
                'github_user': str,
                'id': int,
            }],
            'subscriptions': [{
                'github_repo': str,
                'github_user': str,
                'id': int,
            }]
        },
        'url': str,
        'username': str,
    }
}
