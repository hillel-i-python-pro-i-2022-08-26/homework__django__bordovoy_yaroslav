# Django homework

---

### π install dependencies

_Installing required dependencies._

```
make init-dev
```

### π Run project

_Launch of the project._

```
make homework-i-run
```

### β Purge project

_Delete all created artifacts from run._

```
make homework-i-purge
```

---

## Working with commands

Generates 10 contacts / Generate the requested number of contacts

```
make generate-contacts
-----------------------
python manage.py generate_contacts --amount NUMBER
```

Deletes all contacts / Delete items created less than 30 seconds ago
```
make delete-contacts
---------------------
python manage.py delete_contacts --delete
```

---

## π¦ΈπΌββοΈ Superuser

create superuser

```
make init-dev-i-create-superuser
```

---

## π¦ΈπΌββοΈ Docker


```
make d-homework-i-run
```