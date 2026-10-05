class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> uniq(nums.begin(), nums.end());
        if (nums.size() != uniq.size()) return true;
        return false;
    }
};