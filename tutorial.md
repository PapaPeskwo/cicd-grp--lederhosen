```bash
cd jenkins
docker-compose up -d
```
- `8080:8080` mappar jenkins web interface till 8080 internt och externt
- `50000:50000` mappar jenkins "agent port"

när detta har körts så borde du kunna se jenkins på
http://localhost:8080

## PASSWORD
du kan hitta lösenordet med:
```bash
docker logs jenkins-jenkins-1
```
