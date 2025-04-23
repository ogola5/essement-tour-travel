.PHONY: test
test:
	docker-compose exec backend pytest
	docker-compose exec frontend npm test

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: restart
restart:
	docker-compose restart