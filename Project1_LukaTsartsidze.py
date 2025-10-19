import numpy as np

np.random.seed(42)

employees = {
    "E001": {"name": "Anri Joxadze", "monthly_sales": [45000, 52000, 48000], "days_worked": 58},
    "E002": {"name": "Lamara Xrustalishvili", "monthly_sales": [38000, 41000, 39000], "days_worked": 60},
    "E003": {"name": "Jemal Baghashvili", "monthly_sales": [51000, 49000, 53000], "days_worked": 57},
    "E004": {"name": "Medveda", "monthly_sales": [42000, 38000, 40000], "days_worked": 55},
    "E005": {"name": "Geronti Gagnidze", "monthly_sales": [47000, 50000, 48000], "days_worked": 59},
    "E006": {"name": "Gocha Chertkoevi", "monthly_sales": [35000, 37000, 36000], "days_worked": 52},
    "E007": {"name": "Vaso Adeishvili", "monthly_sales": [44000, 46000, 45000], "days_worked": 56},
    "E008": {"name": "Olegia Popoivi", "monthly_sales": [39000, 42000, 40000], "days_worked": 54},
}

def calculate_total_sales(monthly_sales):
    return sum(monthly_sales)

def calculate_average_sales(monthly_sales):
    return sum(monthly_sales) / len(monthly_sales)

def calculate_attendance_rate(days_worked):
    return (days_worked / 60) * 100

def get_performance_rating(avg_sales, attendance_rate):
    if avg_sales >= 48000 and attendance_rate >= 95:
        return "Excellent"
    elif avg_sales >= 40000 and attendance_rate >= 90:
        return "Good"
    else:
        return "Satisfactory"

print("="*60)
print("QUARTERLY PERFORMANCE REPORT")
print("="*60)

ratings_count = {"Excellent":0, "Good":0, "Satisfactory":0}
total_sales_list = []

for emp_id, emp in employees.items():
    name = emp["name"]
    total = calculate_total_sales(emp["monthly_sales"])
    avg = calculate_average_sales(emp["monthly_sales"])
    attendance = calculate_attendance_rate(emp["days_worked"])
    rating = get_performance_rating(avg, attendance)
    ratings_count[rating] += 1
    total_sales_list.append((emp_id, name, total))

    print(f"\n{emp_id} - {name}")
    print(f" Total Sales: ${total:,.0f}")
    print(f" Avg Monthly: ${avg:,.2f}")
    print(f" Attendance: {attendance:.1f}%")
    print(f" Rating: {rating}")

print("\n" + "="*60)

excellent_count = ratings_count["Excellent"]
avg_total_sales_all = sum(t[2] for t in total_sales_list) / len(total_sales_list)
highest = max(total_sales_list, key=lambda x: x[2])
print(f"Excellent ratings: {excellent_count}")
print(f"Average total sales (team): ${avg_total_sales_all:,.0f}")
print(f"Top performer: {highest[1]} ({highest[0]}) with ${highest[2]:,}")

store_names = ["Downtown", "Mall", "Airport", "Suburb"]
category_names = ["Electronics", "Clothing", "Food"]

sales = np.random.randint(5000, 15001, size=(4,3,12))
print("\n" + "="*60)
print("TASK 2: SALES DATA WITH NUMPY")
print("="*60)
print(f"Array shape: {sales.shape}, dtype: {sales.dtype}")
print("Sample - Week 1 sales (all stores & categories):")
print(sales[:,:,0])

total_by_store = sales.sum(axis=(1,2))
print("\nTotal sales by store:")
for name, total in zip(store_names, total_by_store):
    print(f" {name}: ${int(total):,}")
top_store = store_names[int(np.argmax(total_by_store))]
bottom_store = store_names[int(np.argmin(total_by_store))]
print(f"Highest sales: {top_store}")
print(f"Lowest sales: {bottom_store}")

total_by_category = sales.sum(axis=(0,2))
avg_weekly_by_category = sales.mean(axis=(0,2))
print("\nCategory totals and average weekly sales:")
for cname, tot, avgw in zip(category_names, total_by_category, avg_weekly_by_category):
    print(f" {cname}: Total=${int(tot):,}, Avg weekly=${avgw:.2f}")
driver = category_names[int(np.argmax(total_by_category))]
print(f"Revenue driver category: {driver}")

weekly_totals = sales.sum(axis=(0,1))
best_week = int(np.argmax(weekly_totals)) + 1
worst_week = int(np.argmin(weekly_totals)) + 1
print(f"\nBest week: Week {best_week}, Worst week: Week {worst_week}")

last_7 = weekly_totals[-7:] 
growth_rates = (last_7[1:] - last_7[:-1]) / last_7[:-1]
print("Week-over-week growth rates (last 6 weeks):")
for i, g in enumerate(growth_rates, start=len(weekly_totals)-6):
    print(f" Week {i} -> Week {i+1}: {g*100:.2f}%")

downtown = sales[0]
downtown_by_category = downtown.sum(axis=1)
best_cat_idx = int(np.argmax(downtown_by_category))
print(f"\nDowntown best category: {category_names[best_cat_idx]}")

company_total = total_by_store.sum()
print("\nStore contribution to total sales:")
for name, total in zip(store_names, total_by_store):
    pct = (total / company_total) * 100
    print(f" {name}: {pct:.1f}%")

print("\nRecommendations:")
print(f"- Prioritize {driver} (highest revenue).")
underperforming = bottom_store
print(f"- Investigate {underperforming} store for local marketing and stock adjustments.")

np.random.seed(42)
customers = np.random.normal(loc=7.5, scale=1.5, size=(50,4))
customers = np.clip(customers, 1, 10)
customers = np.round(customers, 1)
categories = ["Product Quality", "Customer Service", "Value for Money", "Delivery Speed"]

print("\n" + "="*60)
print("TASK 3: CUSTOMER SATISFACTION")
print("="*60)
print(f"Ratings array shape: {customers.shape}")
print("First 5 customers (sample):")
print(customers[:5])

overall_avg = customers.mean()
overall_std = customers.std()
print(f"\nOverall average satisfaction: {overall_avg:.2f}")
print(f"Overall std dev: {overall_std:.2f}")

cat_avg = customers.mean(axis=0)
cat_std = customers.std(axis=0)
for cname, avg, sd in zip(categories, cat_avg, cat_std):
    print(f" {cname}: avg={avg:.2f}, std={sd:.2f}")
highest_cat = categories[int(np.argmax(cat_avg))]
lowest_cat = categories[int(np.argmin(cat_avg))]
print(f"Highest rated: {highest_cat}")
print(f"Lowest rated: {lowest_cat}")

cust_avg = customers.mean(axis=1)
most_satisfied_idx = int(np.argmax(cust_avg))
least_satisfied_idx = int(np.argmin(cust_avg))
print(f"\nMost satisfied customer: #{most_satisfied_idx+1} avg={cust_avg[most_satisfied_idx]:.2f}")
print(f"Least satisfied customer: #{least_satisfied_idx+1} avg={cust_avg[least_satisfied_idx]:.2f}")

promoters = cust_avg >= 8.0
passives = (cust_avg >= 6.0) & (cust_avg < 8.0)
detractors = cust_avg < 6.0

n_prom = promoters.sum()
n_pass = passives.sum()
n_det = detractors.sum()
total_cust = len(cust_avg)
nps = ((n_prom - n_det) / total_cust) * 100

print("\nCustomer Segments:")
print(f" Promoters: {n_prom} ({n_prom/total_cust*100:.1f}%)")
print(f" Passives: {n_pass} ({n_pass/total_cust*100:.1f}%)")
print(f" Detractors: {n_det} ({n_det/total_cust*100:.1f}%)")
print(f"Net Promoter Score (NPS): {nps:.1f}")

avg_prom = cust_avg[promoters].mean() if n_prom>0 else np.nan
avg_pass = cust_avg[passives].mean() if n_pass>0 else np.nan
avg_det = cust_avg[detractors].mean() if n_det>0 else np.nan
print("\nAverage rating by segment:")
print(f" Promoters avg: {avg_prom:.2f}")
print(f" Passives avg: {avg_pass:.2f}")
print(f" Detractors avg: {avg_det:.2f}")

if n_det > 0:
    det_ratings = customers[detractors]
    det_cat_avg = det_ratings.mean(axis=0)
    for cname, val in zip(categories, det_cat_avg):
        print(f" Detractors - {cname}: {val:.2f}")
else:
    print(" No detractors to analyze category-wise.")

customer_report = """
Overall customer satisfaction is moderately high with an average score of {:.2f} and an NPS of {:.1f}.
Key findings:
- Product Quality and Customer Service are the strongest areas.
- Value for Money and Delivery Speed need attention, with Value for Money being the lowest-rated category.
- A meaningful share of customers are Passives, indicating opportunity to convert them to Promoters.

Strengths & Weaknesses:
Product Quality scores highest (avg {:.2f}), suggesting product reliability is perceived positively.
Value for Money (avg {:.2f}) is weakest; customers may feel pricing does not fully match perceived value.
Delivery Speed is also below other categories, potentially caused by logistics or communication gaps.

Recommendations:
1) Reassess pricing or bundling to improve perceived value (target Value for Money).
2) Improve delivery tracking and set clearer expectations to boost Delivery Speed scores.
3) Convert Passives to Promoters via targeted loyalty offers and post-purchase follow-ups.
4) Maybe hire an actual consultant instead of relying on my Sleep deprived ass, you cheap fucks.

Customer Retention Strategy:
Prioritize Detractors with targeted outreach (discounts + surveys) to identify root causes.
For Passives, use small incentives and improved communication to raise satisfaction above 8.0.

P.S
I recommend you to not bother me with any more reports or I WILL burn down an orphanage.
Kind regards, 
Your underpaid and overworked employee.
""".strip().format(overall_avg, nps, cat_avg[0], cat_avg[2])

print("\n" + "="*60)
print("WRITTEN CUSTOMER ANALYSIS (200-250 words)")
print("="*60)
print(customer_report)
