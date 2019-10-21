FROM python:latest
ADD UntilTheBirthday/UntilMyBirthday.py /
CMD [ "python", "./UntilMyBirthday.py" ]
