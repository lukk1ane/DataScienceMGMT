import numpy as np
np.random.seed(42)

mean = 7.5
std = 1.5
ratings = np.random.normal(mean, std, (50, 4))

ratings = np.clip(ratings, 1, 10)
print(f"Shape {ratings.shape}")

np.round(ratings, decimals=1)
# print(ratings)

print(f"First Five Customers {ratings[:5]}")

averageSatisfaction = np.mean(ratings)
overallStd = np.std(ratings)

print(f"Average Satisfaction: {averageSatisfaction}")
print(f"Overall Standard Deviation: {overallStd}")

categories = ["Product Quality", "Customer Service", "Value for Money", "Delivery Speed"]

categoriesAvg = np.mean(ratings, axis=0)
categoriesStd = np.std(ratings, axis=0)

for i in range(4):
    print(f"{categories[i]} - Average: {categoriesAvg[i]:.2f} Standard Deviation: {categoriesStd[i]:.2f}")

highestCategory = categories[np.argmax(categoriesAvg)]
lowestCategory = categories[np.argmin(categoriesAvg)]

print(f"Highest Category: {highestCategory}")
print(f"Lowest Category: {lowestCategory}")

customerAvg = np.mean(ratings, axis=1)

most_satisfied = np.argmax(customerAvg)
least_satisfied = np.argmin(customerAvg)

print(f"Most satisfied: {most_satisfied+1}, avg rating {customerAvg[most_satisfied]:.2f}")
print(f"Least satisfied: {least_satisfied+1}, avg rating {customerAvg[least_satisfied]:.2f}")

promoters = np.sum(customerAvg >= 8.0)
passives = np.sum((customerAvg >= 6.0) & (customerAvg < 8.0))
detractors = np.sum(customerAvg < 6.0)

# Segmentation
print(f"Promoters: {promoters}")
print(f"Passives: {passives}")
print(f"Detractors: {detractors}")

# Percentages
total_customers = len(customerAvg)
print(f"Promoters: {promoters / total_customers * 100:.1f}%")
print(f"Passives: {passives / total_customers * 100:.1f}%")
print(f"Detractors: {detractors / total_customers * 100:.1f}%")

promMask = customerAvg >= 8.0
passMask = (customerAvg >= 6.0) & (customerAvg < 8.0)
detMask = customerAvg < 6.0

promIdx = np.where(promMask)[0]
passIdx = np.where(promMask)[0]
detIdx = np.where(promMask)[0]

#  Net Promoter Score
nps = (promoters - detractors) / total_customers * 100
print(f"Net Promoter Score: {nps:.1f}")

#  Average rating for each segment
def mean_or_nan(arr):
    return np.nan if arr.size == 0 else arr.mean()

avgPromoters = mean_or_nan(customerAvg[promMask])
avgPassives = mean_or_nan(customerAvg[promMask])
avgDetractors = mean_or_nan(customerAvg[promMask])


print(f" Promoters average: {avgPromoters:.2f}" if not np.isnan(avgPromoters) else " Promoters average: N/A")
print(f" Passives  average: {avgPassives:.2f}"  if not np.isnan(avgPassives)  else " Passives average: N/A")
print(f" Detractors average: {avgDetractors:.2f}" if not np.isnan(avgDetractors) else " Detractors average: N/A")

# Category performance segment
n_categories = ratings.shape[1]

def category_means_for_mask(mask):
    if np.sum(mask) == 0:
        return np.array([np.nan] * n_categories)
    return np.round(np.mean(ratings[mask, :], axis=0), 2)

cat_means_prom = category_means_for_mask(promMask)
cat_means_pass = category_means_for_mask(promMask)
cat_means_det = category_means_for_mask(promMask)

for i in range(n_categories):
    p = cat_means_prom[i]
    ps = cat_means_pass[i]
    d = cat_means_det[i]
    print(f" {categories[i]:<18} | Promoters: {p if not np.isnan(p) else 'N/A':>5}  | Passives: {ps if not np.isnan(ps) else 'N/A':>5}  | Detractors: {d if not np.isnan(d) else 'N/A':>5}")

# lowest ratings detractors
if detIdx.size == 0:
    print("No detractors in the date")
else:
    detMeans = cat_means_det
    minValue = np.nanmin(detMeans)
    lowestIdxs = np.where(detMeans == minValue)[0]
    lowest_cats = [categories[i] for i in lowestIdxs]
    print(f" Lowest mean rating = {minValue:.2f} for categories: {', '.join(lowest_cats)}")

