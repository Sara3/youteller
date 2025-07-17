# Firefly III + Plaid Integration

## Setup
```bash
docker-compose up -d
```

## Access
- **Firefly III**: http://localhost:83  
- **API**: http://localhost:8000

## Sync Transactions
```bash
curl "http://localhost:8000/api/transactions"
```

## Get Sample Transactions
Plaid sandbox starts empty. To get sample transactions:
1. Go to https://plaid.com/demo/
2. Connect with your Plaid credentials
3. Generate some test transactions
4. Run sync again: `curl "http://localhost:8000/api/transactions"`

Done! 🎉
