#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to pointer of the first node of listint_t
 * @number: Integer value to insert
 *
 * Return: Address of the new node, or NULL if memory allocation fails
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current;

if (head == NULL)
return (NULL);

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
new->next = NULL;

if (*head == NULL || (*head)->n >= number)
{
new->next = *head;
*head = new;
return (new);
}

current = *head;
while (current->next != NULL && current->next->n < number)
current = current->next;

new->next = current->next;
current->next = new;

return (new);
}
