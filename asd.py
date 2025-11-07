
def log_new_tickets(tickets, new_tickets):
    for ticket in new_tickets:
        tickets.append(ticket)


def resolve_tickets(tickets, num_to_resolve):
    resolved = []

    while num_to_resolve > 0 and len(tickets) > 0:
        resolved.append(tickets.pop(0))
        num_to_resolve -= 1

    return resolved


def close_ticket(tickets, ticket_id):
    i = 0
    while i < len(tickets):
        if tickets[i] == ticket_id:
            tickets.pop(i)
            return True
        i += 1
    return False


def manage_tickets(initial_tickets, new_tickets_to_log, tickets_to_resolve, ticket_to_close):
    tickets_copy = initial_tickets[:]      
    log_new_tickets(tickets_copy, new_tickets_to_log)
    close_ticket(tickets_copy, ticket_to_close)
    resolved_list = resolve_tickets(tickets_copy, tickets_to_resolve)

    return tickets_copy, resolved_list

initial = [4501, 4502, 4503, 4504]
new = [4505, 4506]
resolve_count = 2
close_id = 4502

final_state, resolved = manage_tickets(initial, new, resolve_count, close_id)

print("Test Case 1 Results:")
print(f"final_state: {final_state}" )
print(f"resolved: {resolved}")
print(f"Original list (should be unchanged): {initial}")
