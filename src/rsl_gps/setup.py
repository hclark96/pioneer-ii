from setuptools import find_packages, setup

package_name = 'rsl_gps'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='toughbook',
    maintainer_email='toughbook@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'run_gps = rsl_gps.usb_gps_node:main',
            'run_imu = rsl_gps.quat_publisher:main',
            'push_target = rsl_gps.test_position:main',
        ],
    },
)
