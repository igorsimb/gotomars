### Update requirements.txt file
- add new packages to `requirements.in`
- run
```
pip-compile requirements.in
```

### Check deploy settings against production
```
python manage.py check --deploy --settings=config.django.production
```
