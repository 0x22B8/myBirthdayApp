FROM python:latest
LABEL version="v0.4"
ADD ./UntilTheBirthday /UntilTheBirthday
CMD [ "python", "/UntilTheBirthday/UntilMyBirthday.py", "2", "9", "1995" ]
