#### 初始化DJANGO
- setting
```python
ALLOWED_HOSTS = ['*']
# 'django.middleware.csrf.CsrfViewMiddleware', 注释掉改行
```

- 跨机器访问
```
python manage.py runserver 0.0.0.0:8000
```