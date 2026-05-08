from collections import deque, defaultdict

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        max_num = max(nums)
        # 1. Sieve to find primes and smallest prime factor (SPF)
        spf = list(range(max_num + 1))
        for i in range(2, int(max_num**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        def get_prime_factors(num):
            factors = set()
            while num > 1:
                p = spf[num]
                factors.add(p)
                while num % p == 0:
                    num //= p
            return factors

        # 2. Map primes to indices that are multiples of that prime
        prime_to_indices = defaultdict(list)
        for i, x in enumerate(nums):
            # We only care about prime factors of the numbers in nums
            # If x itself is prime, it acts as a teleporter
            temp = x
            while temp > 1:
                p = spf[temp]
                prime_to_indices[p].append(i)
                while temp % p == 0:
                    temp //= p

        # 3. BFS
        queue = deque([(0, 0)]) # (index, distance)
        visited_idx = {0}
        visited_primes = set()
        
        # Precompute which numbers in nums are actually prime
        # (A number is prime if it's > 1 and its smallest prime factor is itself)
        is_prime = [False] * (max_num + 1)
        for x in nums:
            if x > 1 and spf[x] == x:
                is_prime[x] = True

        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
            
            # Option 1: Adjacent steps
            for next_idx in [curr_idx - 1, curr_idx + 1]:
                if 0 <= next_idx < n and next_idx not in visited_idx:
                    visited_idx.add(next_idx)
                    queue.append((next_idx, dist + 1))
            
            # Option 2: Prime Teleportation
            # Only allowed if nums[curr_idx] is prime
            val = nums[curr_idx]
            if is_prime[val] and val not in visited_primes:
                visited_primes.add(val)
                for next_idx in prime_to_indices[val]:
                    if next_idx not in visited_idx:
                        visited_idx.add(next_idx)
                        queue.append((next_idx, dist + 1))
                        
        return -1