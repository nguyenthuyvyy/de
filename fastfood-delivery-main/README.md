# Fastfood Delivery - CI/CD & Monitoring Demo

## 🏗️ Mục tiêu
- Triển khai **CI/CD pipeline** với GitHub Actions: build & test các microservice backend.
- Giám sát trạng thái service bằng **Prometheus** và **Grafana**.
- Dễ dàng mở rộng và maintain cho dự án học thuật hoặc demo thực tế.

---

## 📁 Cấu trúc dự án

fastfood-delivery/
├── backend/
│ ├── order-service/
│ ├── user-service/
│ ├── product-service/
│ └── payment-service/
├── monitoring/
│ └── grafana/
├── docker-compose.yml
├── docker-compose.monitoring.yml
├── prometheus.yml
└── .github/workflows/ci-cd.yml

markdown
Sao chép mã

- Mỗi service backend chạy **FastAPI** độc lập, có endpoint `/health`.
- `docker-compose.yml` chứa tất cả backend service.
- `docker-compose.monitoring.yml` chứa stack Prometheus + Grafana.

---

## 🚀 Hướng dẫn chạy

### 1. Chạy CI/CD (GitHub Actions)
- Mỗi lần **push code lên nhánh `main`**, workflow sẽ:
  1. Build Docker image cho từng service (local only, không push GHCR)
  2. Khởi động container
  3. Kiểm tra endpoint `/health` của từng service
  4. Cleanup container

### 2. Chạy monitoring stack local

```bash
docker-compose -f docker-compose.monitoring.yml up -d
Prometheus: http://localhost:9090

Grafana: http://localhost:3000

Login mặc định: admin/admin

⚙️ Thêm service mới
Tạo folder backend mới, ví dụ review-service.

Tạo Dockerfile và main.py có /health.

Thêm service vào docker-compose.yml.

Thêm tên service vào workflow matrix CI/CD:

yaml
Sao chép mã
strategy:
  matrix:
    service: ["order-service", "payment-service", "product-service", "user-service", "review-service"]
✅ Lợi ích
CI/CD tự động kiểm tra code và trạng thái service.

Monitoring cho phép phát hiện lỗi hoặc downtime sớm.

Demo hoàn toàn chạy local, không cần server cloud.

📌 Lưu ý
Uvicorn trong container port = container port.

Host port trong docker-compose.yml có thể khác để tránh conflict.

Healthcheck + sleep trong CI/CD đảm bảo service khởi động kịp trước khi test.
téttttttt