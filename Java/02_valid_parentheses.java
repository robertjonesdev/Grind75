import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Map;

class Solution {
    public boolean valid_parenthese(String s) {
        Map<Character, Character> charmap = Map.of(
                ')', '(',
                '}', '{',
                ']', '[');
        Deque<Character> stack = new ArrayDeque<>();

        for (char ch : s.toCharArray()) {
            if (!charmap.containsKey(ch)) {
                stack.push(ch);
            } else if (!stack.isEmpty()) {
                char last = stack.pop();
                if (charmap.get(ch) != last) {
                    return false;
                }
            } else {
                return false;
            }
        }

        return stack.isEmpty();
    }
}