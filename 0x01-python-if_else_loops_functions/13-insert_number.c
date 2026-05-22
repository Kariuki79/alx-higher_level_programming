#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: Double pointer to the head of the linked list
 * @number: the integer to insert into the list
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	/* Step 1: Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	/* Step 2: Edge case - empty list or new number is the smallest */
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Step 3: Traverse the list to find the insertion point */
	current = *head;

	/* Look one node ahead to see if we should stop */
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	/* Step 4: Perform the pointer surgery */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
