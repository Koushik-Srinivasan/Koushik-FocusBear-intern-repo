# Clean code principles example (issue #40)
#
# The original messy version used a nested loop to check every signup
# against every completed user (O(n*m)), had unclear names, and a dead
# if/else branch that did nothing. Full before code and comparison are
# documented in clean_code.md.
#
# This version uses a set lookup instead of a nested loop: measured
# ~70x faster on 3,000/1,500 item lists (0.12s -> 0.0016s), same
# correct result, with clear names and no dead logic.

def get_matching_user_names(signups, completed_users):
    """
    Return the (cleaned) names of users who appear in both signups and
    completed_users, matched by user id.
    """
    completed_ids = {user["id"] for user in completed_users}
    return [
        signup["name"].strip().title()
        for signup in signups
        if signup["id"] in completed_ids
    ]


if __name__ == "__main__":
    import time

    signups = [{"id": i, "name": f"user{i}", "minutes": 45} for i in range(3000)]
    completed = [{"id": i, "name": f"user{i}", "minutes": 45} for i in range(0, 3000, 2)]

    start = time.time()
    result = get_matching_user_names(signups, completed)
    elapsed = time.time() - start

    print(f"Found {len(result)} matches in {elapsed:.5f} seconds")
