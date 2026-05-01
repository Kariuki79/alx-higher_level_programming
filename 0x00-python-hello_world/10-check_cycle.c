#include "lists.h"

/**
 * check_cycle - checks if a slightly linked list has a cycle in it
 * @list: pointer to the end of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* If the list is empty, there can't be a cycle */
	if (list == NULL)
		return (0);

	/* Loop continues as long as fast pointer hasn't hit the end (NULL) */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If they land on the exact same node, there is a cycle */
		if (slow == fast)
			return (1);
	}

	/* If the loop breaks, the fast pointer hit the end, No cycle. */
	return (0);
}
