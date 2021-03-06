defaults_main_data = """
---
testcase: "*"
test_cases: []

nitro_user: nsroot
nitro_pass: nsroot
"""

tasks_main_data = """
---
- { include: nitro.yaml, tags: ['nitro'] }
"""

tasks_main_data_with_testbed = """
---
- { include: testbed.yaml, state: present }
- { include: nitro.yaml, tags: ['nitro'] }
- { include: testbed.yaml, state: absent }
"""

tasks_nitro_data = """
- name: collect all nitro test cases
  find:
    paths: "{{ role_path }}/tests/nitro"
    patterns: "{{ testcase }}.yaml"
  register: test_cases

- name: set test_items
  set_fact: test_items="{{ test_cases.files | map(attribute='path') | list }}"

- name: run test case
  include: "{{ test_case_to_run }}"
  with_items: "{{ test_items }}"
  loop_control:
    loop_var: test_case_to_run
"""
