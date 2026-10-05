class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> uniq(nums.begin(), nums.end());
        return nums.size() != uniq.size();
    }
};