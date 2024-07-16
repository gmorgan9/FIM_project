from setuptools import setup, find_packages

setup(
    name='fim_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'fim_tool = fim_tool.automate:main',
        ],
    },
    author='Garrett Morgan',
    author_email='garrett.morgan@morganserver.com',
    description='File Integrity Monitoring tool with Slack notifications',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gmorgan9/FIM_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)
