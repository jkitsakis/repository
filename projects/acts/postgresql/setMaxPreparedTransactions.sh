#!/bin/bash

sed -i 's/^.*max_prepared_transactions\s*=\s*\(.*\)$/max_prepared_transactions = 100\t\t#\1/' /var/lib/postgresql/data/postgresql.conf