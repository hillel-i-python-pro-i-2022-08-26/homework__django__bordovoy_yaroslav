# Django homework

---

### 🔄 install dependencies

_Installing required dependencies._

```
make init-dev
```

### 🚀 Run project

_Launch of the project._

```
make homework-i-run
```

### ❌ Purge project

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

## 🦸🏼‍♂️ Superuser

create superuser

```
make init-dev-i-create-superuser
```

---

## 🦸🏼‍♂️ Docker


```
make d-homework-i-run
```

## 🦸🏼‍♂️ Drf CRUD


```
/api/contacts/  --- view all contacts (API)
/api/create/   --- create a contact (API)
/api/update/contact_pk   --- update contact (API)
/api/delete/contact_pk   --- delete contact (API)
/api/showcontact_pk   --- view contact (API)
```