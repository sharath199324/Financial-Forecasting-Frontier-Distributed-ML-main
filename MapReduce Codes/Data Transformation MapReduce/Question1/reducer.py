#!/usr/bin/env python
import sys

current_job_type = None
current_balance_total = 0
current_count = 0

for line in sys.stdin:
    try:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t')
        if len(parts) != 2:
            print(f"SKIPPING: bad line: {line}", file=sys.stderr)
            continue

        job_type, account_balance = parts
        account_balance = float(account_balance)

        if current_job_type == job_type:
            current_balance_total += account_balance
            current_count += 1
        else:
            if current_job_type is not None:
                average_balance = current_balance_total / current_count
                print(f'{current_job_type}\t{average_balance:.2f}')

            current_job_type = job_type
            current_balance_total = account_balance
            current_count = 1

    except Exception as e:
        print(f"Reducer Error: {e} | line: {line}", file=sys.stderr)
        continue

if current_job_type is not None and current_count > 0:
    average_balance = current_balance_total / current_count
    print(f'{current_job_type}\t{average_balance:.2f}')
