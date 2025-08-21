#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the end of the list
 * @number: number to insert
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	/* Case 1: Insert at the beginning or empty list */
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* Case 2: Traverse until correct position */
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* Insert new node */
	new->next = current->next;
	current->next = new;

	return (new);
}
