#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of he singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 *
 * Description: This function implements Floyd's Tortoise and Hare algorithm.
 * It uses two pointers, one moving at a slow pace (one step at a time)
 * and another moving at a fast pace (two steps at a time). if the list
 * contains a cycle, the fast pointer will eventually catch up to the slow
 * pointer. If there is no cycle, the fast pointer will reach the end of
 * the list (NULL).
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p;
	listint_t *fast_p;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	slow_p = list;
	fast_p = list;


	while (fast_p != NULL && fast_p->next != NULL)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (fast_p == slow_p)
		{
			return (1);
		}
	}
	return (0);
}
