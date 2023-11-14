# Jenkins

```bash
cd jenkins
docker-compose up -d
```
- `8080:8080` mappar jenkins web interface till 8080 internt och externt
- `50000:50000` mappar jenkins "agent port"

när detta har körts så borde du kunna se jenkins på
http://localhost:8080

# requirements.txt

```bash
pip install -r requirements.txt
```

# pylint

```bash
pylint <file>.py
```

för att köra wildcard mot alla py filer, kör:
```bash
pylint **/*.py
```

# black

```bash
black <file>.py
```

för att köra wildcard mot alla py filer, kör:
```bash
black **/*.py
```
